from django.urls import path
from django.shortcuts import redirect
from . import views

app_name = 'brews'

urlpatterns = [
    path('', views.index, name='index'),
]
