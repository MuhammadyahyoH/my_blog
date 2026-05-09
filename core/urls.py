from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core_home.urls')),
    path('', include('accounts.urls')),
    path('blog/', include('blog.urls')),
    path('likes/', include('likes.urls')),
    path('projects/', include('projects.urls')),
    path('contact/', include('contact.urls')),
    path('api-auth/', include('rest_framework.urls')),  # ✅ DRF login
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)