
from django.shortcuts import render

from topdriver.models import Driver


def topdriverstime(request):
    toptime = Driver.objects.all()
    return render(request, "toplaptime.html", {"toptime": toptime})
