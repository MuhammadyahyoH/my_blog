from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from blog.models import Post
from .models import Like

@login_required
def like_post(request, pk):
    post = Post.objects.get(id=pk)

    liked = False

    if Like.objects.filter(user=request.user, post=post).exists():
        # ❌ Unlike
        Like.objects.filter(user=request.user, post=post).delete()
        liked = False
    else:
        # ❤️ Like
        Like.objects.create(user=request.user, post=post)
        liked = True

    return JsonResponse({
        "likes": post.likes.count(),
        "liked": liked
    })