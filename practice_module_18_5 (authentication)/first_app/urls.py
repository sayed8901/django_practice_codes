from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('profile/', views.profile, name='profile'),

    path('pass_change/', views.password_change, name='pass_change'),
    path('pass_change_2/', views.password_change_2, name='pass_change_2'),
]
