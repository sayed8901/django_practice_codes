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



# class based views for adding musician
@method_decorator(login_required, name='dispatch')
class AddMusicianView(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'musician.html'
    success_url = reverse_lazy('homepage')
    

# class based views for editing musician
@method_decorator(login_required, name='dispatch')
class EditMusicianView(UpdateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = 'musician.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('homepage')

