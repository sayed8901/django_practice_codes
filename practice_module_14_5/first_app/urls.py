from django.urls import path
from . import views

urlpatterns = [
    path('form1', views.form_API),
    path('form2', views.model_form),
]
