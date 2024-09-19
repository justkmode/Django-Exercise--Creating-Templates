# myproject/urls.py

from django.contrib import admin
from django.urls import path, include  # include is needed to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),  # Include your app's URLs
]
