from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import logout


def home(request):
    return render(request, 'home_page.html')

def logout_view(request):
    logout(request)
    return render(request, 'logout_page.html')

def create_account(request):
    #If we get a post request we will accept the form data, else create blank form
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}! You are now able to log in.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'create_account.html', {'form': form})