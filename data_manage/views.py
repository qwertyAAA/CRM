from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse,FileResponse
from data_manage import models
from django.apps import apps
from django.utils.http import urlquote
from Myutils.pageutil import Page
import os
# Create your views here.

def check(request):
    datalist=models.Data.objects.all()
    #得到当前app下面的data类
    head=apps.get_model('data_manage','Data')
    #得到data类中的所有字段
    headobj=head._meta.fields
    headname=[]
    keyword=''
    search_fields=['id','data_name']
    for i in headobj:
        headname.append(i.verbose_name)
    # print(search_field)
    #搜索
    if request.method=='POST':
        keyword=request.POST.get('keyword',None)
        search_field=headobj
        from django.db.models import Q
        search_q = Q()
        search_q.connector = "or"
        for search_field in search_fields:
            # try:
            search_q.children.append((search_field+ "__icontains", keyword))
            # except Exception:
            #     search_q.children.append(('data_name'+ "__icontains", keyword))
        datalist = models.Data.objects.all().filter(search_q)
        print('datalist',datalist)
        if datalist==None:
            datalist=''
    page=Page(datalist,request,9,10)
    sum=page.Sum()
    return render(request,'data_manage/check_data.html',{'datalist':sum[0],'headname':headname,'keyword':keyword,'page_html':sum[1]})

def checkdata(request,id):
        data=models.Data.objects.filter(id=id)[0]
        if data.comment:
            #文件后缀
            index = data.comment.name.rindex('.')
            filesuffix = data.comment.name[index:]
            #文件名字
            nameindex=data.comment.name.rindex('/')
            filename=data.comment.name[nameindex+1:]
            #转换为响应头可以传输的编码类型
            newfilename=urlquote(filename)
        else:
            filesuffix = '文件为空'
            filename='文件为空'
        #文件下载
        if request.method == 'POST':
            path = data.comment.path
            print(path)
            with open(path, 'rb') as f:
                my_down = f.read()
                response = HttpResponse(my_down)
                # response = FileResponse(my_down)#有待解决,fileresponse下载的都是ASCII值
                response['Content-Type'] = 'application/octet-stream;charset=utf-8'
                response['Content-Disposition'] = 'attachment;filename=%s'%newfilename
            return response
        return render(request,'data_manage/check_onedata.html',{'data':data,'filesuffix':filesuffix,'filename':filename})


def add(request):
    # print(request.GET.items())
    categorylist=models.Category.objects.all()
    if request.method=='POST':
        checkbox=request.POST.get('checkbox')
        print('checkbox:',checkbox)
        dataname=request.POST.get('dataname')
        categoryid=request.POST.get('category')
        category=models.Category.objects.filter(id=categoryid).first()
        datausername=request.POST.get('datauser')
        datauser=models.User.objects.filter(username=datausername)[0]
        print(datauser.username)
        datafile=request.FILES.get('datafile')
        newdata=models.Data.objects.create(data_name=dataname,category=category,comment=datafile,user=datauser,user_id=datauser.id)
        return redirect('/data_manage/check/')
    return render(request,'data_manage/add_data.html',{'category':categorylist})

def delete(requset):
    if requset.method=='GET':
        dataid=requset.GET.get('id')
        data=models.Data.objects.filter(id=dataid)[0]
        if data.comment:
            filepath=data.comment.path
            if os.path.exists(filepath):  # 如果文件存在
                os.remove(filepath)  # 则删除
        data.delete()
        return redirect('/data_manage/check/')
    else:
        idlist=requset.POST.getlist('idlist')
        #全选操作时,前端传过来的idlist里面有一个空字符,需要删除
        try:
            idlist.remove('')
        except Exception:
            pass
        for id in idlist:
            data = models.Data.objects.filter(id=int(id))[0]
            if data.comment:
                filepath = data.comment.path
                if os.path.exists(filepath):  # 如果文件存在
                    os.remove(filepath)  # 则删除
            data.delete()
        return JsonResponse({'test':1})

def edit(requset,id):
    if requset.method=='GET':
        dataid=id
        data=models.Data.objects.get(id=dataid)
        categorylist = models.Category.objects.all()
        #文件后缀
        if data.comment:
            index=data.comment.name.rindex('.')
            filesuffix=data.comment.name[index:]
        else:
            filesuffix='文件为空'
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
        if newdata.comment:
            filepath=newdata.comment.path
            if os.path.exists(filepath):  # 如果文件存在
                # 删除文件，可使用以下两种方法。
                os.remove(filepath)  # 则删除

        newdata.data_name=dataname
        newdata.comment = datafile
        newdata.category=category
        newdata.user=datauser
        newdata.save()
        return redirect('/data_manage/check/')

def cheak_category(request):
    category_list = models.Category.objects.all()
    if request.method=='POST':
        keyword=request.POST.get('keyword',None)
        search_fields=['id','title']
        from django.db.models import Q
        search_q = Q()
        search_q.connector = "or"
        for search_field in search_fields:
            # try:
            search_q.children.append((search_field+ "__icontains", keyword))
            # except Exception:
            #     search_q.children.append(('data_name'+ "__icontains", keyword))
        category_list = models.Category.objects.all().filter(search_q)
    page = Page(category_list, request, 9, 10)
    sum = page.Sum()
    return render(request,'data_manage/check_category.html',{'category_list':sum[0],'page_html':sum[1]})

def add_category(request):
    title=models.Category.objects.all().values('title')
    titlelist=[]
    for i in title:
        titlelist.append(i['title'])
    print(titlelist)
    if request.method=='POST':
        category_name=request.POST.get('category_name')
        models.Category.objects.create(title=category_name)
        return redirect('/data_manage/check_category/')
    return render(request,'data_manage/add_category.html',{'titlelist':titlelist})

def delete_category(request):
    if request.method=='GET':
        categoryid=request.GET.get('id')
        category=models.Category.objects.filter(id=categoryid)[0]
        category.delete()
        return redirect('/data_manage/check_category/')
    else:
        idlist=request.POST.getlist('idlist')
        print(idlist)
        #全选操作时,前端传过来的idlist里面有一个空字符,需要删除
        try:
            idlist.remove('')
        except Exception:
            pass
        for id in idlist:
            category = models.Category.objects.filter(id=id)[0]
            category.delete()
        return JsonResponse({'test':1})

def edit_category(request,id):
    category=models.Category.objects.filter(id=id)[0]
    title = models.Category.objects.all().values('title')
    titlelist = []
    for i in title:
        titlelist.append(i['title'])
    if request.method=='POST':
        categorytitle=request.POST.get('category_name')
        categoryid=request.POST.get('category_id')
        newcategory=models.Category.objects.get(id=categoryid)
        newcategory.title=categorytitle
        newcategory.save()
        return redirect('/data_manage/check_category')
    return render(request,'data_manage/edit_category.html',{'titlelist':titlelist,'categroy':category})