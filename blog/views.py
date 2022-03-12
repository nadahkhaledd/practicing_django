from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'page.html', {'posts': posts})

def post(request):
    return HttpResponse('post page')
