# blog/admin.py
from django.contrib import admin
from .models import BlogPost, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published', 'created_at')
    list_filter = ('published', 'created_at', 'tags')
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('tags',)
