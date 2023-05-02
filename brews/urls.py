from django.urls import path

app_name = 'brews'

urlpatterns = [
    path('', 'brews/index.html', name='index'),
]
