from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    search_fields = ['title', 'body']
    list_filter = ['created_at']
    ordering = ['-created_at']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'text', 'created_at']
    list_filter = ['created_at']
    search_fields = ['text', 'user__username']
    ordering = ['-created_at']