from multiprocessing import context
from django.shortcuts import render
from django.shortcuts import render
# I imported Owners model
from . models import Owners

# owner_list will return Owners model's all objects 

def owner_list(request):
    # ('-date') provides showing up last added object 
    owners = Owners.objects.all().order_by('-date')
    # I created library structure for key, value pairs
    context = {
        'owners': owners
    }

    return render(request, "owners.html", context)
