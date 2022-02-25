from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("dashboard/", views.user_dashbord, name="dashboard"),
    path("logut/", views.user_logout, name="logout"),
    path("enroll_the_anımal/", views.enroll_the_anımal, name="enroll_the_anımal"),
    path('release_the_anımal/', views.release_the_anımal,name="release_the_anımal"),
]
