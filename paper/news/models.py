from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from django.utils import timezone


class Author(models.Model):
    authorUser = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    ratingAuthor = models.SmallIntegerField(default=0)

    def update_rating(self):
        postRat = self.authorUser.post_set.all().aggregate(postRating=Sum('rating'))
        pRat = postRat.get('postRating', 0)

        commentRat = Comment.objects.filter(user=self.authorUser).aggregate(commentRating=Sum('rating'))
        cRat = commentRat.get('commentRating', 0)

        self.ratingAuthor = pRat * 3 + cRat
        self.save()

    def __str__(self):
        return self.authorUser.username


class Category(models.Model):
    name = models.CharField(
        max_length=64,
        unique=True,
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        default=1
    )
    news = 'NW'
    article = 'AR'
    CHOICES = {
        news: 'новость',
        article: 'статья'
    }
    postType = models.CharField(
        max_length=2,
        choices=CHOICES,
        default='NW'
    )

    dateCreation = models.DateTimeField(default=timezone.now)
    category = models.ManyToManyField(
        Category,
        through='PostCategory'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Название'
    )
    text = models.TextField(
        max_length=100,
        verbose_name='Описание'
    )

    rating = models.SmallIntegerField(default=0)

    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        length = 124
        if len(self.text) <= length:
            return self.text + '...'
        else:
            return self.text[:length] + '...'

    def __str__(self):
        return f'{self.title}: {self.text}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=50)
    dateCreation = models.DateTimeField(default=timezone.now)
    rating = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.user.username

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


from django.db import models

# Create your models here.
