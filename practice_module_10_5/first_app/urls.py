from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_home),
    path('about/', views.about),
    path('contact/', views.contact),
]
