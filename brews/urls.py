from django.urls import path
from . import views

app_name = 'brews'

urlpatterns = [
    path('', views.index, name='index'),
]
