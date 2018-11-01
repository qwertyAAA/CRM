from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from data_manage import models
from django.apps import apps
import os
# Create your views here.

def check(request):
    datalist=models.Data.objects.all()
    head=apps.get_model('data_manage','Data')
    headobj=head._meta.fields
    headname=[]
    for i in headobj:
        headname.append(i.verbose_name)
    # print(headname)
    # print(headname.verbose_name)
    if request.method=='POST':
        pass
    return render(request,'data_manage/check_data.html',{'datalist':datalist,'headname':headname})

def add(request):
    categorylist=models.Category.objects.all()
    if request.method=='POST':
        checkbox=request.POST.get('checkbox')
        print('checkbox:',checkbox)


        dataname=request.POST.get('dataname')
        categoryid=request.POST.get('category')
        category=models.Category.objects.filter(id=categoryid).first()
        datausername=request.POST.get('datauser')
        datauser=models.User.objects.filter(username=datausername).first()
        datafile=request.FILES.get('datafile')
        # print('datafile:',datafile)
        newdata=models.Data.objects.create(data_name=dataname,category=category,comment=datafile,user=datauser)
        return redirect('/data_manage/add/')
    return render(request,'data_manage/add_data.html',{'category':categorylist})

def delete(requset):
    dataid=requset.GET.get('id')
    data=models.Data.objects.filter(id=dataid)[0]
    data.delete()
    return redirect('/data_manage/check/')

def edit(requset):
    if requset.method=='GET':
        dataid=requset.GET.get('id')
        data=models.Data.objects.get(id=dataid)
        categorylist = models.Category.objects.all()
        #文件后缀
        index=data.comment.name.rindex('.')
        filesuffix=data.comment.name[index:]
        return render(requset, 'data_manage/edit.html',
                      {
                          'dataid':data.id,
                          'dataname': data.data_name,
                          'categorytitle': data.category.title,
                          'datauser': data.user.username,
                          'datafile': data.comment,
                          'categorylist': categorylist,
                          'filesuffix': filesuffix,
                      })
    # if requset.method=='POST':
    else:
        dataname=requset.POST.get('dataname')
        daid =requset.POST.get('daid')

        categoryid =requset.POST.get('category')
        category = models.Category.objects.filter(id=categoryid).first()

        datausername =requset.POST.get('datauser')
        datauser = models.User.objects.filter(username=datausername).first()

        datafile =requset.FILES.get('datafile')
        print(daid)
        newdata=models.Data.objects.get(id=daid)

        #删除原来的文件
        filepath=newdata.comment.path
        if os.path.exists(filepath):  # 如果文件存在
            # 删除文件，可使用以下两种方法。
            os.remove(filepath)  # 则删除

        # print('dataname:',dataname,'categoryid:',categoryid,'datausername:',datausername)
        newdata.data_name=dataname
        newdata.comment = datafile
        # newdata.category.set(category)
        newdata.category=category
        # newdata.user.set(datauser)
        newdata.user=datauser
        newdata.save()
        return redirect('/data_manage/check/')
