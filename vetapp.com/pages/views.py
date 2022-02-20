from django.shortcuts import render

# index func for requesting index.html
def index(request):
    return render(request,"index.html")

# anımals func for requesting anımals.html
def anımals(request):
    return render(request, "anımals.html")

