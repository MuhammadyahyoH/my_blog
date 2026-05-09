from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import like_post
from .api_views import LikeViewSet

router = DefaultRouter()
router.register(r'likes', LikeViewSet)

urlpatterns = [
    path('<int:pk>/like/', like_post, name='like_post'),
    path('api/', include(router.urls)),
]