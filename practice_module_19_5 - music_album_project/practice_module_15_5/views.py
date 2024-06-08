from django.shortcuts import render
from album.models import Album

# Create your views here.
def home(request):
    album_data = Album.objects.all()

    return render(request, 'home.html', context={'data': album_data})

