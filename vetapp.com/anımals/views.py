from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import render
# I imported Anımals model
from . models import Anımals

# anımal_list will return Anımals model's all objects

def anımal_list(request):
    # ('-date') provides showing up last added object
    anımals = Anımals.objects.all().order_by('-date')
    # I created library structure for key, value pairs
    context = {
        'anımals' : anımals
    }

    return render(request, "anımals.html",context)
