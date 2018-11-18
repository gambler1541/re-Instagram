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
    # render하는 경우
    #   1. POST요청이며, 사용자명이 이미 존재할 경우
    #   2. POST요청이며, 비밀번호가 같지 않은 경우
    #   3. GET요청인 경우
    # redirect하는 경우
    #   1. POST요청이며, 사용자명이 존재하지 않고 비밀번호가 같은 경우
    """
    if request.method가 POST면:
        if 사용자명이 존재하면:
            render
        if 비밀번호가 같지 않으면:
            render
        (else, POST면서 사용자도없고 비밀번호도 같으면):
            redirect
    (else, GET요청이면):
        render

    if request.method가 POST면:
        if 사용자명이 존재하면:
        if 비밀번호가 같지 않으면:
        (else, POST면서 사용자도없고 비밀번호도 같으면):
            redirect
    (else, GET요청이면):
        render


    :return:
    """
    context ={
        'form':SignupForm(),
    }
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if User.objects.filter(username=username).exists():
            context['error'] = f'{username}은 이미 사용중입니다.'
        elif password1 != password2:
            context['error'] = '비밀번호를 확인해 주세요.'
        else:
            user = User.objects.create_user(
                username=username,
                password=password1,
            )
            login(request, user)
            return redirect('posts:post_list')

    return render(request, 'members/signup.html', context)