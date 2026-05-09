from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import login_view, register_view, logout_view
from .api_views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('api/', include(router.urls)),
]