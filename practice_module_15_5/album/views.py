from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def home(request):
    if request.method == 'POST':
        album_data = forms.AlbumForm(request.POST)

        if album_data.is_valid():
            album_data.save()
            print(album_data)
            return redirect('homepage')
        
    else:
        album_data = forms.AlbumForm
    
    return render(request, 'album.html', {'form': album_data})



def edit_album(request, id):
    target_album = models.Album.objects.get(pk=id)
    print(target_album)

    album_form = forms.AlbumForm(instance=target_album)

    if request.method == 'POST':
        album_form = forms.AlbumForm(request.POST, instance=target_album)

        if album_form.is_valid():
            album_form.save()
            print(album_form.cleaned_data)

            return redirect('homepage')

    return render(request, 'album.html', {'form': album_form})



def delete_album(request, id):
    target_album = models.Album.objects.get(pk=id).delete()
    print(target_album)

    return redirect('homepage')

