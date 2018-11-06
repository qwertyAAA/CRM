from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from user_management import models
from django.contrib.auth.models import User


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
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        if password == confirm_password:
            User.objects.create_user(username=username, password=password)
        return redirect("/index/")

    return render(request, "user_management/edit_user.html")


def search_user(request):
    if request.is_ajax():
        key = request.POST.get("key")
        value = request.POST.get("value")
        ret = {"status": False, "html": ""}
        if len(value) == 0:
            return JsonResponse(ret)
        # 我实在没有办法找到一个更为简便的方法来处理这个问题
        # 思路：利用反射，将key反射为filter方法的参数名（双下划线查询的内容），但行不通
        # 而且当前端返回的是全部时，该如何查询？这已经算要构建一个搜索引擎了吧。。。。。。。。。
        if key == "用户编号":
            result = User.objects.filter(id=value)
        elif key == "用户名":
            result = User.objects.filter(username__icontains=value)
        elif key == "管理员分类":
            result = User.objects.filter(role__role_name__icontains=value)
        elif key == "员工姓名":
            result = User.objects.filter(staff__staff_name__icontains=value)
        elif key == "部门名称":
            result = User.objects.filter(staff__staff_name__icontains=value)
        elif key == "创建日期":
            result = User.objects.filter(date_joined=value)
        elif key == "职位名称":
            result = User.objects.filter(staff__staff_job__icontains=value)
        elif key == "职务级别":
            result = User.objects.filter(staff__staff_job_level__icontains=value)
        else:
            result = None
        if result:
            qs = result.values(
                "id",
                "username",
                "role__role_name",
                "staff__staff_name",
                "staff__department__department_name",
                "date_joined",
            )
            # 这一步，同样是找不到合适的处理方法，为了代码的简化以及可读性，我选择在后端创建好一个html后返回前端
            ret["status"] = True
            ret["html"] = "<tr name='table_item'>"
            for item in qs:
                ret["html"] += '''
                <td><input type="checkbox" class="check_item"></td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                '''.format(
                    item["id"],
                    item["username"],
                    item["role__role_name"],
                    item["staff__staff_name"],
                    item["staff__department__department_name"],
                    item["date_joined"]
                )
            ret["html"] += "</tr>"
        return JsonResponse(ret)
    return render(request, "user_management/search_user.html")


def user_info(request):
    return render(request, "user_management/user_info.html")


def role_permission(request):
    return render(request, "user_management/role_permission.html")


def edit_role(request):
    if request.method == "POST":
        pass
    return render(request, "user_management/edit_role.html")


def check_data(request):
    if request.is_ajax():
        ret = {"status": True, "msg": "!!!!!!!!!!!!!!!!!!!!!!!"}
        return JsonResponse(ret)
