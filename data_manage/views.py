from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from data_manage import models

# Create your views here.

def check(request):
    datalist=models.Data.objects.all()
    if request.method=='POST':
        pass
    return render(request,'data_manage/check_data.html',{'datalist':datalist})