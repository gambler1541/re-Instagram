from django.shortcuts import redirect

def index(request):
    return redirect('posts:post_list')