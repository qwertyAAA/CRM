from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.


def index(request):
    return render(request, "main_page/index.html")


def login(request):
    return render(request, "main_page/login.html")
