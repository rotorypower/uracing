import logging
from django.shortcuts import redirect, render

from trackday.models import Post

logger = logging.getLogger(__name__)


def trackday_post(request):
    if request.user.is_anonymous:
        return redirect("admin:index")
    posts = Post.objects.all()
    return render(request, "trackday.html", {"posts": posts})


def post_view(request, post_id):
    posts = Post.objects.get(id=post_id)
    return render(request, "trackpost.html", {"post": posts})