from django.shortcuts import render, get_object_or_404, redirect
from itertools import groupby
from collections import defaultdict
from .models import Post, Comment


def post_list(request):
    posts = Post.objects.all()

    grouped = defaultdict(lambda: defaultdict(list))
    for post in posts:
        year = post.created_at.year
        month = post.created_at.strftime('%B')
        grouped[year][month].append(post)

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


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    if request.user == comment.user:
        comment.delete()
    return redirect(request.META.get('HTTP_REFERER', '/'))