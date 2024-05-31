from django.shortcuts import render
from . import forms
from . import forms

# Create your views here.

def form_API(request):
    if request.method == 'POST':
        form = forms.sample_form(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
    
    else:
        form = forms.sample_form

    return render(request, 'form_API.html', {'form': form})



def model_form(request):
    if request.method == 'POST':
        form = forms.sample_model_form(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
    
    else:
        form = forms.sample_model_form

    return render(request, 'model_form.html', {'form': form})