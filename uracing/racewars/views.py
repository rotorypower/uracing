from django.shortcuts import render

from racewars.models import FotoContent


def foto(request):
    racefotos = FotoContent.objects.all()
    return render(request, 'racewarscontent/racewars.html', {'racefotos': racefotos})
