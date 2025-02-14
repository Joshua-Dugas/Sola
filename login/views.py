from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def login(request):
    template = loader.get_template('login_page.html')
    return HttpResponse(template.render())

def create_account(request):
    template = loader.get_template('create_account.html')
    return HttpResponse(template.render())