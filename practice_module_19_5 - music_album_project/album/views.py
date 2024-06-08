from django.shortcuts import render, redirect
from . import forms
from . import models

# necessary importing for class view implementation
from django.views.generic import CreateView, UpdateView, DeleteView

# to use login required decorator
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# importing reverse_lazy to redirect
from django.urls import reverse_lazy



# class based views for adding album
@method_decorator(login_required, name='dispatch')
class AddAlbumView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album.html'
    success_url = reverse_lazy('homepage')


# class based views for editing album
@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')


# class based views for editing album
@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')


