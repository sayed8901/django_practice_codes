from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def home(request):
    if request.method == 'POST':
        musician_data = forms.MusicianForm(request.POST)

        if musician_data.is_valid():
            musician_data.save()
            print(musician_data)
            return redirect('homepage')
        
    else:
        musician_data = forms.MusicianForm
    
    return render(request, 'musician.html', {'form': musician_data})



def edit_musician(request, id):
    target_musician = models.Musician.objects.get(pk=id)
    print(target_musician)

    musician_form = forms.MusicianForm(instance=target_musician)

    if request.method == 'POST':
        musician_form = forms.MusicianForm(request.POST, instance=target_musician)

        if musician_form.is_valid():
            musician_form.save()
            print(musician_form.cleaned_data)

            return redirect('homepage')

    return render(request, 'musician.html', {'form': musician_form})