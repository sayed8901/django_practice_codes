from django.urls import path
from . import views

urlpatterns = [
    path('', views.AddAlbumView.as_view(), name='album'),
    path('edit_album/<int:id>', views.EditAlbumView.as_view(), name='edit_album'),
    path('delete_album/<int:id>', views.DeleteAlbumView.as_view(), name='delete_album'),
]
