from django.shortcuts import render, redirect
from . forms import LoginFrom, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == 'POST':
        # We equalized from to LoginForm class Which is in forms.py
        form = LoginFrom(request.POST)
        #
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

    if request.method == 'POST':
        form = RegisterForm(request.POST)
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
    return redirect('index')


@login_required(login_url='login')
def user_dashbord(request):
    current_user = request.user
    return render(request, 'dashboard.html')
