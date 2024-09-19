# myapp/urls.py

from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
]
