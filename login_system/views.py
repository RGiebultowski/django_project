from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'login_system/home.html', context)

def about(request):
    return render(request, 'login_system/about.html', {'title': 'About'})


