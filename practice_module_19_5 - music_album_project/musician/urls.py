from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddMusicianView.as_view(), name='musician'),
    path('edit_musician/<int:id>', views.EditMusicianView.as_view(), name='edit_musician'),
]
