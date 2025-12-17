# blog/urls.py
from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('tag/<slug:tag_slug>/', BlogListView.as_view(), name='tag'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='detail'),
]
