from django.shortcuts import render


def index(request):
    return render(request,"index.html")


def anımals(request):
    return render(request, "anımals.html")

