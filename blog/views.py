from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from .models import Post, Comment


def post_list(request):
    posts = Post.objects.all()

    # Yil va oyga guruhlash
    from itertools import groupby
    from collections import defaultdict

    grouped = defaultdict(lambda: defaultdict(list))
    for post in posts:
        year = post.created_at.year
        month = post.created_at.strftime('%B')
        grouped[year][month].append(post)

    # dict ga o'tkazish (template uchun)
    grouped_posts = {
        year: dict(months)
        for year, months in sorted(grouped.items(), reverse=True)
    }

    return render(request, 'blog/post_list.html', {
        'grouped_posts': grouped_posts,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()

    # Oldingi va keyingi post
    prev_post = Post.objects.filter(id__lt=pk).order_by('-id').first()
    next_post = Post.objects.filter(id__gt=pk).order_by('id').first()

    if request.method == "POST":
        text = request.POST.get('text')
        if request.user.is_authenticated and text:
            Comment.objects.create(post=post, user=request.user, text=text)
            return redirect('post_detail', pk=post.pk)

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'prev_post': prev_post,
        'next_post': next_post,
    })

from .models import Comment

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)

    # faqat comment egasi o‘chira olsin
    if request.user == comment.user:
        comment.delete()

    return redirect(request.META.get('HTTP_REFERER', '/'))

from datetime import date
from blog.models import Post
from projects.models import Project
from .models import About

def about_me(request):
    about = About.objects.first()

    context = {
        "about": about,
        "projects_count": Project.objects.count(),
        "posts_count": Post.objects.count(),
        "years_learning": date.today().year - 2024,  # start year
    }

    return render(request, "aboutme.html", context)

