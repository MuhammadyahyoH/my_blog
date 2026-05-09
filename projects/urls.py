from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import project_list
from .api_views import ProjectViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', project_list, name='project_list'),
    path('api/', include(router.urls)),
]