from django.shortcuts import render, redirect
from . forms import LoginFrom, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from anımals.models import Anımals


def user_login(request):
    if request.method == 'POST':
        # We equalized from to LoginForm class Which is in forms.py
        form = LoginFrom(request.POST)
        # if form is valid and there is, app is redirecting to index.html template
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username,
                                password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('index')

                else:
                    messages.info(request, 'User is not Active')
            else:
                messages.info(request, 'Username or Password is wrong')
    else:
        form = LoginFrom()
    return render(request, 'login.html', {'form': form})


def user_register(request):
    # When 'POST' method comes with request to  user_register, it checks is it validiable
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # if it is validiable shows up a message and redirecting to login page
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Account has been created, You can LOGIN')
            return redirect('login')

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def user_logout(request):
    logout(request)
    # logout func get request as a paramether it redirecting to index page
    return redirect('index')


@login_required(login_url='login')
def user_dashbord(request):
    current_user = request.user

    anımals = current_user.Animal_added.all()

    context = {
        'anımals': anımals
    }

    return render(request, 'dashboard.html', context)


def enroll_the_anımal(request):
    anımal_id = request.POST['anımal_id']
    user_id = request.POST['user_id']
    anımal = Anımals.objects.get(id=anımal_id)
    user = User.objects.get(id=user_id)
    anımal.owners.add(user)
    return redirect('dashboard')


def release_the_anımal(request):
    anımal = Anımals.objects.get(id=request.POST['anımal_id'])
    user = User.objects.get(id=request.POST['user_id'])
    anımal.owners.remove(user)
    return redirect('dashboard')
