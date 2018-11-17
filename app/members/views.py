from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, passwrod=password)
        if user is not None:
            login(request, user)
            return redirect('posts:post_list')
        else:
            return HttpResponse('ID 또는 Password를 확인하십시오')
    else:
        form = LoginForm()
        context = {
            'form' : form
        }
        return render(request, 'members/login.html', context)

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('posts:post_list')