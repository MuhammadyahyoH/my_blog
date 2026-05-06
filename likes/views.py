from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Like

@login_required
def like_post(request, pk):
    post = Post.objects.get(id=pk)

    like_obj = Like.objects.filter(user=request.user, post=post).first()

    if like_obj:
        # ❌ unlike
        like_obj.delete()
        liked = False
    else:
        # ❤️ like
        Like.objects.create(user=request.user, post=post)
        liked = True

    return JsonResponse({
        "likes": post.likes.count(),
        "liked": liked
    })