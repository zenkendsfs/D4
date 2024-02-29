from django_filters import FilterSet, CharFilter, ModelMultipleChoiceFilter, DateFilter
from .models import Post, Author
from django.forms import DateInput


class PostFilter(FilterSet):
    title = CharFilter(
        field_name='title',
        label='Загаловок',
        lookup_expr='icontains',
    )
    category = ModelMultipleChoiceFilter(
        queryset=Post.objects.all(),
        field_name='category',
        label='Категория',
    )
    dateCreation = DateFilter(
        field_name='dateCreation',
        label='С даты',
        lookup_expr='gte',
        widget=DateInput(attrs={
            'type': 'date',
            'id': 'dateCreation',
            'name': 'dateCreation',
        })
    )