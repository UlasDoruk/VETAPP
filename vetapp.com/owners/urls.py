from django import views
from django.urls import path
# Importing ListView and DetailView classes
from owners.views import OwnersListView, OwnersDetailView

urlpatterns = [
    path("",OwnersListView.as_view(),name="owners"),
    # Assigned primary key to all owners 
    path('owners/<int:pk>',OwnersDetailView.as_view(),name="owners_detail")
]


""" # I imported vetapp/views.py 
from . import views

# When vetapp/urls.py call the owners/urls.py, urlpatterns list showed the path of owner_list function

urlpatterns = [
    path('', OwnerListView.as_view(), name="teachers"),

] """
