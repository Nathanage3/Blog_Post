from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

posts = [
    {'author': 'Sisay',
     'title': 'Blog Post 1',
     'content': 'First post content',
     'date_posted': 'May 12, 2024'
     },
    {'author': 'Nathan',
     'title': 'Blog Post 2',
     'content': 'Second post content',
     'date_posted': 'May 11, 2024'
     },
]

# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/about.html')