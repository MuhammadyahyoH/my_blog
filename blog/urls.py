from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import post_list, post_detail, delete_comment
from .api_views import PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:pk>/', post_detail, name='post_detail'),
    path('comment/delete/<int:pk>/', delete_comment, name='delete_comment'),
    path('api/', include(router.urls)),
]