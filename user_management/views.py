from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# Create your views here.


def users_list(request):
    return HttpResponse("this is user_list")


def test(request):
    return render(request, "MOM.html")


def create_user(request):
    return render(request, "user_management/create_user.html")
