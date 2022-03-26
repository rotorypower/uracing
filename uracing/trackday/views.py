import logging
from django.http import HttpResponse
from django.shortcuts import redirect, render

from trackday.models import Post

logger = logging.getLogger(__name__)


def trackday_post(request):
   if request.user.is_anonymous:
      return redirect("admin:index")
   posts = Post.objects.all()
   return render(request, "trackday.html", {"posts":posts})