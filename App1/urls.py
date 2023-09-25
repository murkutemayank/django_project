# appname/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('file-upload/', views.file_upload, name='file_upload'),
    # Add other URL patterns as needed
]+static(settings.MEDIA_URL,document_root=settings.MRDIA_ROOT)
