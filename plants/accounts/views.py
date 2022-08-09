from django.shortcuts import render
from django.http import HttpResponse


# Функции и классы, активирующие наши шаблоны URL
# Create your views here.

def home(request):
    return render(request, 'accounts/dashboard.html')

def room(request):
    return render(request, 'accounts/room.html')

def plants(request):
    return render(request, 'accounts/plantsBD.html')

def history(request):
    return render(request, 'accounts/history.html')
