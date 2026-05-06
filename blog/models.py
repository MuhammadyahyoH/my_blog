from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count()  # agar related_name="likes" bo‘lsa

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:30]


class About(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.name