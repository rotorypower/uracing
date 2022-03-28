
from django.shortcuts import render

from topdriver.models import Driver


def topdriverstime(request):
    toptimes = Driver.objects.all()
    return render(request, "toptime/toplaptime.html", {"toptimes": toptimes})
