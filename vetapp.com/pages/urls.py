from functools import partial
from django.urls import path
from . import views

# Connectting urlpatterns elements to views.py

urlpatterns = [
    path('', views.index,name="index"),
    path('anımals', views.anımals, name="anımals"),
]