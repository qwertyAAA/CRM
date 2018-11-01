from django.shortcuts import render, HttpResponse, redirect


# Create your views here.
# 机构信息列表
def organ_list(request):
    return render(request, "organization/organ_list.html")
