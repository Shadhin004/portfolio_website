from django.shortcuts import render
from django.http import HttpResponse
from .models import experience


def index(request):
    exp = experience.objects.all()
    return render(request, 'exp.html', {'x': exp})


def home(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def hobby(request):
    return render(request, 'hobby.html')