from django.shortcuts import render

# Create your views here.
def app_home(request):
    data = {
        'age': 20,
        'bio': 'Hello, This is Sayed from Naraynagnaj',
        'text_list': ['Hello', 'I', 'am', 'Sayed.']
    }
    return render(request, 'home.html', context = data)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')