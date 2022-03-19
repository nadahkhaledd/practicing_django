from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'page.html', {'posts': posts})

def post(request, URLSlug):
    print('-->', URLSlug)
    return render(request, 'post.html', {
        'post': get_object_or_404(Post, URLSlug=URLSlug)
    })

def about(request):
    return render(request, 'about.html', )
