from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-id')

    if request.method == "POST":
        text = request.POST.get('text')

        if request.user.is_authenticated and text:
            Comment.objects.create(
                post=post,
                user=request.user,
                text=text
            )
            return redirect('post_detail', pk=post.id)

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments
    })