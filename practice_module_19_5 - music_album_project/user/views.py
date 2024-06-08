from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages

# necessary importing for class view implementation
from django.contrib.auth.views import LoginView, LogoutView

# importing reverse_lazy to redirect
from django.urls import reverse_lazy



# Create your views here.
def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully')

            return redirect('register')
    
    else:
        register_form = forms.RegistrationForm()

    return render(request, 'register.html', {'form': register_form,  'type': 'Register'})




# login using class based view
class UserLoginView(LoginView):
    template_name = 'register.html'
    # success_url = reverse_lazy('profile')

    def get_success_url(self) -> str:
        return reverse_lazy('homepage')

    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Login information incorrect')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'login'
        return context
    



# logout using class based view
class UserLogoutView(LogoutView):
    def get_success_url(self) -> str:
        return reverse_lazy('login')


