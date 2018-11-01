from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from data_manage import models
from django.apps import apps
# Create your views here.

def check(request):
    datalist=models.Data.objects.all()
    head=apps.get_model('data_manage','Data')
    headobj=head._meta.fields
    # print(headname.verbose_name)
    if request.method=='POST':
        pass
    return render(request,'data_manage/check_data.html',{'datalist':datalist})