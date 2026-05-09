from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import date
from blog.models import Post
from projects.models import Project
from .models import About


def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('register')


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard.html')


def about_me(request):
    about = About.objects.first()
    context = {
        'about': about,
        'projects_count': Project.objects.count(),
        'posts_count': Post.objects.count(),
        'years_learning': date.today().year - 2024,
    }
    return render(request, 'aboutme.html', context)