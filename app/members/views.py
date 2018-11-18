from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm,SignupForm

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

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).exists():
            return HttpResponse(f'{username}은 이미 사용중입니다.')
        if password1 != password2:
            return HttpResponse('비밀번호를 확인하여 주십시요.')

        user = User.objects.create_user(
            username=username,
            password=password1,
        )
        login(request, user)
        return redirect('posts:post_list')
    else:
        form = SignupForm()
        context = {
            'form' : form
        }
        return render(request, 'members/signup.html', context)