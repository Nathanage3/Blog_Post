from django.http import HttpResponse, HttpRequest
from .models import Post
from django.shortcuts import render


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/about.html')