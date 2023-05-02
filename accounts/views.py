from django.shortcuts import render, redirect
from .forms import UserCreate, UserChange
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('brews:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@login_required()
def logout(request):
    auth_logout(request)
    return redirect('brews:index')

def signup(request):
    if request.method == 'POST':
        form = UserCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('brews:index')
    else:
        form = UserCreate()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@login_required()
def modify(request):
    if request.method == 'POST':
        form = UserChange(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:modify')
    else:
        form = UserChange(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/modify.html', context)
