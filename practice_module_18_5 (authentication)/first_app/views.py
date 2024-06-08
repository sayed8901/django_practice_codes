from django.shortcuts import render, redirect
from .forms import Resisterform, ChangeUserData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = Resisterform(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been created successfuly!')
                return redirect('login')
        else:
            form = Resisterform()

        return render(request,'signup.html', {'form':form})
    
    else:
        return redirect('profile')

    

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request, data = request.POST)

            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                user = authenticate(username = user_name, password = user_password)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'You have been logged in successfuly!')
                    return redirect('profile')
                
        else:
            form = AuthenticationForm()
        
        return render(request, 'login.html', {'form':form})
    
    else:
        return redirect('profile')
    



def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangeUserData(request.POST, instance = request.user)

            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been updated successfuly!')
                return redirect('login')
            
        else:
            form = ChangeUserData(instance = request.user)
        
        return render(request, 'profile.html', {'form':form})
     
    else:
        return redirect('signup')



def user_logout(request):
    logout(request)
    return redirect('login')



def password_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(data = request.POST, user = request.user)

            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                messages.success(request, 'Your password has been updated successfuly!')
                return redirect('profile')
        
        else:
            form = PasswordChangeForm(user = request.user)
        
        return render(request, 'password_change.html', {'form':form})
    
    else:
        return redirect('login')



def password_change_2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user, data = request.POST)

            if form.is_valid():
                form.save()
                # password update korbe
                update_session_auth_hash(request, form.user)

                return redirect('profile')
            
        else:
            form = SetPasswordForm(user = request.user)
            
        return render(request, 'password_change.html', {'form': form})
    
    else:
        return redirect('login')
    


