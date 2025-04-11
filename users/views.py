from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from users.forms import UserLoginForm, UserRegistrationForm


def log_in(request) -> HttpResponseRedirect | HttpResponse:
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = UserLoginForm()

    context: dict = {
        'title': 'Home - Авторизация',
        'form': form
    }
    return render(request, "login.html", context)


def register_user(request) -> HttpResponse:
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return HttpResponseRedirect(reverse('user:profile'))
        
    else:
        form = UserRegistrationForm()
    context: dict[str, str] = {
        'title': 'Home - Регистрация',
         'form': form
    }
    return render(request, "register.html", context)


def profile_user(request) -> HttpResponse:
    context: dict[str, str] = {
        'title': 'Home - Профиль'
    }
    return render(request, "profile.html", context)


@login_required
def logout_user(request):
    messages.success(request, f"{request.user.username}, Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))