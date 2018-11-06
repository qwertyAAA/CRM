from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
'''当导入这个方法的时候：用的时候必须是  models.表明'''
from employee_management import models
from django.apps import apps

''' 当导入这个时候跟上面的区别是直接用不用加.'''
# from .models import *
from django import forms
from django.forms import widgets

from django.forms import ModelForm


# class StaffForm(ModelForm):
#     class Meta:
#
#         model=models.Staff
#         fields="__all__"
#         labels={"staff_salary":"员工薪资",'staff_state':"员工状态"}
#         widgets={
#             "staff_salary":widgets.TextInput(attrs={"class":"form-control"}),
#             "staff_state":widgets.TextInput(attrs={"class":"form-control"}),
#
#         }
#         error_messages={
#             "staff_state":{"required":'不能为空'}
#         }
#


def add_employee(request):
    if request.method == "POST":
        em_eusername = request.POST.get('username')


        em_email = request.POST.get('email')
        em_password = request.POST.get('password')
        em_staff_salary=request.POST.get('staff_salary')
        em_department_id_list = request.POST.getlist('department_id_list')
        # user=models.User.objects.create(username=em_eusername,email=em_email,password=em_password)

        staff=models.Staff.objects.create(staff_salary=em_staff_salary)
        # staff.department=em_department_id_list

        staff_obj=models.Staff.objects.create(staff_salary=em_staff_salary)
        staff_obj.authors.add(*em_department_id_list)

        return redirect("/employee_info/")

    department_list = models.Department.objects.all()
    staff_list = models.Staff.objects.all()
    # if request.method=="POST":
    #     form=StaffForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #
    #
    #     # return render(request,"employee_management/add_employee.html")
    #
    # form=StaffForm()
    return render(request, "employee_management/add_employee.html", locals())


def main(request):
    return render(request, "MOM.html")


def employee_info(request):
    department_list=models.Department.objects.all()
    staff_list = models.Staff.objects.all()

    return render(request, "employee_management/employee_info.html", locals())


def edit_employee(request):
    if request.method == "POST":
        pass
    return render(request, "employee_management/edit_employee.html")
