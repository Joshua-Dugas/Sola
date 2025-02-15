from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def login(request):
    template = loader.get_template('login_page.html')
    return HttpResponse(template.render())

def create_account(request):
    #If we get a post request we will accept the form data, else create blank form
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            return redirect('login')


    else:
        form = UserCreationForm()
    return render(request, 'create_account.html', {'form': form})