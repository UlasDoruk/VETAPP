from django.urls import path
# I imported vetapp/views.py
from . import views

# When vetapp/urls.py call the anımals/urls.py, urlpatterns list showed the path of anımal_list function

urlpatterns = [
    path('', views.anımal_list, name="anımals"),
    
]
