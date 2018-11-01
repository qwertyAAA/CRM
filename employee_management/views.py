from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from employee_management import models
# Create your views here.
from django.apps import apps

def users_list(request):
    return HttpResponse("this is user_list")


def test(request):
    return render(request, "MOM.html")


def check(request):
    datalist=models.Data.objects.all()
    head=apps.get_model('data_manage','Data')
    headobj=head._meta.fields
    # print(headname.verbose_name)
    if request.method=='POST':
        pass
    return render(request,'data_manage/check_data.html',{'datalist':datalist})