from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('category.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
