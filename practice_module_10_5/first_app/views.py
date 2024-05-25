from django.shortcuts import render

# Create your views here.
def app_home(request):
    data = {
        'age': 20,
        'bio': 'Hello, This is Sayed from Naraynagnaj',
        'text_list': ['Hello', 'I', 'am', 'Sayed.'],
        'courses': [
            {
                'id': 1,
                'name': 'Mathematics',
                'fee': 2000
            },
            {
                'id': 2,
                'name': 'Physics',
                'fee': 2500
            },
            {
                'id': 3,
                'name': 'English',
                'fee': 3000
            },
        ]
    }
    return render(request, 'home.html', context = data)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')