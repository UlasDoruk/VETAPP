from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.user_login, name="login"),
    path("register/", views.user_register, name="register"),
    path("dashboard/", views.user_dashbord, name="dashboard"),
    path("logut/", views.user_logout, name="logout"),
]
