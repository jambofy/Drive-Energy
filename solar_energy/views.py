from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import SolarPanel, Order

def index(request):
    return render(request, 'index.html')

def projects(request):
    return render(request, 'projects.html')

def products(request):
    return render(request, 'products.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')