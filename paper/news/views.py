from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author
from .forms import PostForm
from django.urls import reverse_lazy
from .filters import PostFilter


class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 10


    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'poste.html'
    context_object_name = 'post'


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'
    context_object_name = 'post'

    def form_valid(self, form):
        current_url = self.request.path
        post = form.save(commit=False)
        if current_url == '/news/create/':
            post.postType = 'NW'
        else:
            post.postType = 'AR'
        return super().form_valid(form)


class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'

    # def form_valid(self, form):
    #     post = form.save(commit=False)
    #     post.postType = 'NW'


class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
from django.shortcuts import render

# Create your views here.
