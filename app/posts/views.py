from django.http import HttpResponse
from django.shortcuts import render

def post_list(request):
    return HttpResponse('Post-List!!!!')
