from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.


def auth(request):
    if request.method == "POST":
        pass
    return render(request, "user_management/auth.html")


def change_pwd(request):
    if request.method == "POST":
        pass
    return render(request, "user_management/change_pwd.html")


def edit_user(request):
    if request.method == "POST":
        pass
    return render(request, "user_management/edit_user.html")


def search_user(request):
    if request.method == "POST":
        pass
    return render(request, "user_management/search_user.html")


def user_info(request):
    return render(request, "user_management/user_info.html")


def role_permission(request):
    return render(request, "user_management/role_permission.html")


def edit_role(request):
    if request.method == "POST":
        pass
    return render(request, "user_management/edit_role.html")