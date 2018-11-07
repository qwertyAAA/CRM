from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from user_management import models
from django.contrib.auth.models import User
from django.db.models import Q


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
    username = request.POST.get("username")
    password = request.POST.get("password")
    confirm_password = request.POST.get("confirm_password")
    if request.is_ajax():
        error = {"status": False, "msg": ""}
        result = User.objects.filter(username=username)
        if result.exists():
            error = {"status": True, "msg": "用户名已存在"}
        if password != confirm_password:
            error = {"status": True, "msg": "两次输入的密码不一致"}
        return JsonResponse(error)
    elif request.method == "POST":
        if password == confirm_password:
            User.objects.create_user(username=username, password=password)
        return render(request, "user_management/edit_user.html", {"create_user_status": True})
    return render(request, "user_management/edit_user.html", {"create_user_status": False})


def search_user(request):
    keys = [
        ["all", "全部"],
        ["id", "用户编号"],
        ["username", "用户名"],
        ["role__role_name", "管理员分类"],
        ["staff__staff_name", "员工姓名"],
        ["staff__department__department_name", "部门名称"],
        ["date_joined", "创建日期"],
        ["staff__staff_job", "职位名称"],
        ["staff__staff_job_level", "职务级别"]
    ]
    if request.is_ajax():
        key = request.POST.get("key")
        value = request.POST.get("value")
        ret = {"status": False, "html": ""}
        if len(value) == 0:
            return JsonResponse(ret)
        q = Q()
        q.connector = "or"
        if key == "all":
            keys.pop(0)
            for item in keys:
                q.children.append((item[0] + "__icontains", value))
        else:
            q.children.append((key + "__icontains", value))
        result = models.User.objects.filter(q).values(
            "id",
            "username",
            "role__role_name",
            "staff__staff_name",
            "staff__department__department_name",
            "date_joined",
        )
        ret["status"] = True
        for item in result:
            ret["html"] += '''
                <tr name='table_item'>
                <td><input type="checkbox" class="check_item"></td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                <td>{}</td>
                </tr>
                '''.format(
                item["id"],
                item["username"],
                item["role__role_name"],
                item["staff__staff_name"],
                item["staff__department__department_name"],
                item["date_joined"].strftime("%Y-%m-%d %H:%M:%S")
            )
        return JsonResponse(ret)
    return render(request, "user_management/search_user.html", {"keys": keys})


def user_info(request):
    return render(request, "user_management/user_info.html")


def role_permission(request):
    return render(request, "user_management/role_permission.html")


def edit_role(request):
    if request.method == "POST":
        pass
    return render(request, "user_management/edit_role.html")
