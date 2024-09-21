from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def user_login(request):

    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            user = None

        if user and user.check_password(raw_password=password):
            login(request, user)
            messages.success(request, f"Xush kelibsiz, {request.user.username} !")
            return redirect("/")
        else:
            messages.error(request, "Username yoki Parol xato")

    return render(request, "app_users/login.html")


def user_logout(request):
    logout(request)
    messages.info(request, "Tizimdan chiqdingiz")
    return redirect("/users/login/")


def user_registration(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not username:
            messages.error(request, "Username bo'sh bo'lishi mumkin emas")
            return redirect("/users/login/")

        user_exists = len(User.objects.filter(username=username)) == 1

        if not user_exists:
            if (password1 == password2):
                user = User.objects.create(username=username)
                user.set_password(raw_password=password2)
                user.save()
                messages.success(request, "Akkaunt muvaffaqiyatli yaratildi")
                return redirect("/users/login/")
            else:
                messages.error(request, "Parollar har xil, bir xil bo'lishi shart")
                return redirect("/users/registration/")
        else:
            messages.error(request, "Username allaqachon olingan")
            return redirect("/users/registration/")

    return render(request, "app_users/registration.html")