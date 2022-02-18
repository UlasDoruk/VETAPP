from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import render
from . models import Anımals

def anımal_list(request):
    anımals = Anımals.objects.all().order_by('-date')

    context = {
        'anımals' : anımals
    }

    return render(request, "anımals.html",context)
