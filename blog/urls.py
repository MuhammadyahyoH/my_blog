from django.urls import path
from .views import post_list, post_detail, delete_comment, like_post

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('comment/delete/<int:pk>/', delete_comment, name='delete_comment'),
    path('<int:pk>/like/', like_post, name='like_post'),
]