from django.urls import path
from .views import (PostList, PostDetail, PostCreate, PostUpdate, PostDelete)

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('search/', PostList.as_view(), name='search'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
]