from django.urls import path
# I imported vetapp/views.py 
from . import views

# When vetapp/urls.py call the owners/urls.py, urlpatterns list showed the path of owner_list function

urlpatterns = [
    path('', views.owner_list, name="owners"),

]
