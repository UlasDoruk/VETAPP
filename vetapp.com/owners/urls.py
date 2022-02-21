from . import views
from django.urls import path
# Importing ListView and DetailView classes
from owners.views import OwnersListView, OwnersDetailView

urlpatterns = [
    path("",OwnersListView.as_view(),name="owners"),
    # Assigned primary key to all owners 
    path('owners/<int:pk>',OwnersDetailView.as_view(),name="owners_detail"),
    path('search/', views.search, name='search')
]

