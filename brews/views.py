from django.shortcuts import render, redirect
from . import views


def index(request):
    return render(request, 'brews/index.html')