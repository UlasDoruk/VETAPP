from django.urls import path
# Imported all things of vetapp/views.py
from . import views
from anımals.views import AnımalsListView, AnımalsDetailView 

urlpatterns = [
    path("", AnımalsListView.as_view(), name="anımals"),
    # Assigned primary key to all anımals (<int:pk>
    path('anımals/<int:pk>', AnımalsDetailView.as_view(), name="anımals_detail"),
    path('search/',views.search,name='search')
]
