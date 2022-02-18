from django.urls import path
from . import views

urlpatterns = [
    path('', views.anımal_list, name="anımals"),
    
]
