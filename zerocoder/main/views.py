from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render (request, 'main/index.html', {'caption':"Django"})

def new(request):
    return render(request, 'main/new.html')

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def services(request):
    return render(request, 'main/services.html')

def contact(request):
    return render(request, 'main/contact.html')