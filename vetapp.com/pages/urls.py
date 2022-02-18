from functools import partial
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('anımals', views.anımals, name="anımals"),
]