"""
URL configuration for the samke project.

This file defines URL routes for the Django project,
including admin routes, customer app routes, and media serving during development.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),  # Include routes from customers app
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

