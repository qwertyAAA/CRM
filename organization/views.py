from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect, JsonResponse
from .models import *
from django.apps import apps
import json


# Create your views here.
# 机构信息列表
def organ_view(request):
    organ_list = Organ.objects.all()
    model_obj = apps.get_model("organization", "Organ")
    organ_field = model_obj._meta.fields
    header_list = []

    for f in organ_field:
        header_list.append(f.verbose_name)
    print(header_list)
    return render(request, "organization/organ_list.html", {"header_list": header_list, "organ_list": organ_list})


# 创建机构信息
def organ_add(request):
    if request.method == "POST":
        org_name = request.POST.get("org_name", None)
        print(org_name, "orgname", None)
        org_address = request.POST.get("org_address", None)
        mobile = request.POST.get("mobile", None)
        tel = request.POST.get("tel", None)
        country = request.POST.get("country", None)
        province = request.POST.get("province", None)
        city = request.POST.get("city", None)
        postcode = request.POST.get("postcode", None)
        site = request.POST.get("site", None)
        industry = request.POST.get("industry", None)
        area_level = request.POST.get("area_level", None)
        agent = request.POST.get("agent", None)
        pur_level = request.POST.get("pur_level", None)
        pur_way = request.POST.get("pur_way", None)
        distribution = request.POST.get("distribution", None)
        check_status = request.POST.get("check_status", None)
        org_category = request.POST.get("org_category", None)
        follow_status = request.POST.get("follow_status", None)
        remark = request.POST.get("remark", None)
        tag = request.POST.get("tag", None)
        org_obj = Organ.objects.create(org_name=org_name, org_address=org_address,
                                       mobile=mobile, tel=tel, country=country, province=province, city=city,
                                       postcode=postcode, site=site, industry=industry, area_level=area_level,
                                       agent=agent, pur_level=pur_level, pur_way=pur_way, distribution=distribution,
                                       check_status=check_status, org_category=org_category,
                                       follow_status=follow_status,
                                       remark=remark, tag=tag)
        return redirect(to="/organization/detail/%s" % org_obj.id)
    return render(request, "organization/organ_add.html")


# 编辑机构信息
def organ_edit(request, id):
    org_id = int(id)
    if request.method == "POST":
        org_id = int(id)
        org_name = request.POST.get("org_name", None)
        print(org_name, "orgname", None)
        org_address = request.POST.get("org_address", None)
        mobile = request.POST.get("mobile", None)
        tel = request.POST.get("tel", None)
        country = request.POST.get("country", None)
        province = request.POST.get("province", None)
        city = request.POST.get("city", None)
        postcode = request.POST.get("postcode", None)
        site = request.POST.get("site", None)
        industry = request.POST.get("industry", None)
        area_level = request.POST.get("area_level", None)
        agent = request.POST.get("agent", None)
        pur_level = request.POST.get("pur_level", None)
        pur_way = request.POST.get("pur_way", None)
        distribution = request.POST.get("distribution", None)
        check_status = request.POST.get("check_status", None)
        org_category = request.POST.get("org_category", None)
        follow_status = request.POST.get("follow_status", None)
        remark = request.POST.get("remark", None)
        tag = request.POST.get("tag", None)
        Organ.objects.filter(id=org_id).update(
            org_name=org_name, org_address=org_address,
            mobile=mobile, tel=tel, country=country, province=province, city=city,
            postcode=postcode, site=site, industry=industry, area_level=area_level,
            agent=agent, pur_level=pur_level, pur_way=pur_way, distribution=distribution,
            check_status=check_status, org_category=org_category,
            follow_status=follow_status,
            remark=remark, tag=tag
        )
        return redirect(to="/organization/detail/%s" % org_id)
    organ_obj = Organ.objects.filter(id=org_id).first()
    return render(request, "organization/organ_edit.html", {"organ_obj": organ_obj})


# 机构信息详情
def organ_detail(request, id):
    if request.method == "GET" and request.is_ajax() == False:
        org_id = int(id)
        org_obj = Organ.objects.filter(id=org_id).first()
        if org_obj:
            return render(request, "organization/organ_detail.html", {"org_obj": org_obj})
    elif request.is_ajax():
        org_id = int(id)
        # org_obj = json.dumps(Organ.objects.get(id=org_id))
        # org_obj = "厦门大学"
        org_obj = list(Organ.objects.filter(id=org_id).values(
            "org_name", "org_address", "mobile", "tel", "country", "province", "city",
            "postcode", "site", "industry", "area_level", "agent", "pur_level", "pur_way",
            "distribution", "check_status", "org_category", "follow_status", "remark", "tag"
        ))
        if org_obj:
            print(org_obj, "***********")
            return JsonResponse(org_obj, safe=False)


# 搜索机构信息
def organ_search(request):
    if request.method == "POST":
        search_key = request.POST.get("search_key", None)
        print(search_key,"********")
        header = request.POST.get("header", None)
        if header == "机构名称":
            organ_list = Organ.objects.filter(org_name__icontains=search_key)
        elif header == "省份":
            organ_list = Organ.objects.filter(province__icontains=search_key)
        elif header == "城市":
            organ_list = Organ.objects.filter(city__icontains=search_key)
        elif header == "行业类别":
            organ_list = Organ.objects.filter(industry__icontains=search_key)
        elif header == "分配情况":
            organ_list = Organ.objects.filter(distribution__icontains=search_key)
        elif header == "机构类型":
            organ_list = Organ.objects.filter(org_category__icontains=search_key)
        elif header == "跟进状态":
            organ_list = Organ.objects.filter(follow_status__icontains=search_key)
        return render(request, "organization/organ_search.html", {"organ_list": organ_list, "header": header})


# 联系人列表
def linkman_view(request):
    linkman_list = Linkman.objects.all()
    model_obj = apps.get_model("organization", "Linkman")
    linkman_field = model_obj._meta.fields
    header_list = []

    for f in linkman_field:
        header_list.append(f.verbose_name)
    print(header_list)
    return render(request, "organization/linkman_list.html", {"header_list": header_list, "linkman_list": linkman_list})


# 创建联系人
def linkman_add(request):
    if request.method == "POST":
        org_name = request.POST.get("organ_name", None)
        organ_obj = Organ.objects.filter(org_name=org_name).first()
        name = request.POST.get("name", None)
        gender = request.POST.get("gender", None)
        duty = request.POST.get("duty", None)
        phone = request.POST.get("phone", None)
        email = request.POST.get("email", None)
        QQ = request.POST.get("qq", None)
        adress = request.POST.get("adress", None)
        link_important = request.POST.get("link_important", None)
        following = request.POST.get("following", None)
        link_agent = request.POST.get("link_agent", None)
        isaccept = request.POST.get("isaccept", None)
        remark = request.POST.get("remark", None)
        link_obj = Linkman.objects.create(organ=organ_obj, name=name, gender=gender, duty=duty,
                                          phone=phone, email=email, QQ=QQ, adress=adress, link_important=link_important,
                                          following=following, link_agent=link_agent, isaccept=isaccept, remark=remark)
        return redirect(to="/organization/linkman_detail/%s/" % link_obj.id)
    return render(request, "organization/linkman_add.html")


# 编辑联系人
def linkman_edit(request, id):
    linkman_id = int(id)
    if request.method == "POST":
        org_name = request.POST.get("organ_name", None)
        organ_obj = Organ.objects.filter(org_name=org_name).first()
        name = request.POST.get("name", None)
        gender = request.POST.get("gender", None)
        duty = request.POST.get("duty", None)
        phone = request.POST.get("phone", None)
        email = request.POST.get("email", None)
        QQ = request.POST.get("QQ", None)
        adress = request.POST.get("adress", None)
        link_important = request.POST.get("link_important", None)
        following = request.POST.get("following", None)
        link_agent = request.POST.get("link_agent", None)
        isaccept = request.POST.get("isaccept", None)
        remark = request.POST.get("remark", None)
        link_obj = Linkman.objects.filter(id=linkman_id).update(
            organ_id=organ_obj.id, name=name, gender=gender, duty=duty,
            phone=phone, email=email, QQ=QQ, adress=adress, link_important=link_important,
            following=following, link_agent=link_agent, isaccept=isaccept, remark=remark
        )
        return redirect(to="/organization/linkman_detail/%s" % linkman_id)
    linkman_obj = Linkman.objects.filter(id=linkman_id).first()
    return render(request, "organization/linkman_edit.html", {"linkman_obj": linkman_obj})


# 联系人详情
def linkman_detail(request, id):
    if request.method == "GET" and request.is_ajax() == False:
        linkman_id = int(id)
        linkman_obj = Linkman.objects.filter(id=linkman_id).first()
        if linkman_obj:
            return render(request, "organization/linkman_detail.html", {"linkman_obj": linkman_obj})
    elif request.is_ajax():
        linkman_id = int(id)
        linkman_obj = list(Linkman.objects.filter(id=linkman_id).values(
            "organ__org_name", "name", "gender", "duty", "phone", "email", "QQ",
            "adress", "link_important", "following", "link_agent", "isaccept", "remark"
        ))
        if linkman_obj:
            print(linkman_obj, "***********")
            return JsonResponse(linkman_obj, safe=False)


#删除联系人
def linkman_delete(request, id):
    linkman_id = int(id)
    Linkman.objects.filter(id=linkman_id).delete()
    linkman_list = Linkman.objects.all()
    model_obj = apps.get_model("organization", "Linkman")
    linkman_field = model_obj._meta.fields
    header_list = []
    for f in linkman_field:
        header_list.append(f.verbose_name)
    return render(request, "organization/linkman_list.html", {"linkman_list": linkman_list, "header_list": header_list})


#删除机构信息
def organ_delete(request, id):
    organ_id = int(id)
    Organ.objects.filter(id=organ_id).delete()
    organ_list = Organ.objects.all()
    model_obj = apps.get_model("organization", "Organ")
    organ_field = model_obj._meta.fields
    header_list = []

    for f in organ_field:
        header_list.append(f.verbose_name)
    return render(request, "organization/organ_list.html", {"organ_list": organ_list, "header_list": header_list})

# 搜索联系人
def linkman_search(request):
    if request.method == "POST":
        search_key = request.POST.get("search_key", None)
        print(search_key,"********")
        header = request.POST.get("header", None)
        if header == "机构名称":
            linkman_list = Linkman.objects.filter(organ__org_name__icontains=search_key)
        elif header == "姓名":
            linkman_list = Linkman.objects.filter(name__icontains=search_key)
        elif header == "性别":
            linkman_list = Linkman.objects.filter(gender__icontains=search_key)
        elif header == "重要等级":
            linkman_list = Linkman.objects.filter(link_important__icontains=search_key)
        elif header == "跟进状态":
            linkman_list = Linkman.objects.filter(following__icontains=search_key)
        return render(request, "organization/linkman_search.html", {"linkman_list": linkman_list, "header": header})


#添加联系人时检查机构名是否可添加
def org_name_check(request):
    if request.method == "POST":
        data = {}
        name = request.POST.get("organ_name", None)
        print("要添加的机构名称：", name)
        if Organ.objects.filter(org_name=name):
            if Linkman.objects.filter(organ__org_name=name):
                data["message"] = "该机构已创建联系人，要修改请返回编辑页面！"
            else:
                data["message"] = "该机构尚未创建联系人，可以直接创建！"
        else:
            data["message"] = "该机构信息尚未创建，请先创建该机构信息！"
    return JsonResponse(data, safe=False)


#添加机构信息时检查机构名是否已添加
def org_name_check2(request):
    if request.method == "POST":
        data = {}
        name = request.POST.get("organ_name", None)
        print("要添加的机构名称：", name)
        if Organ.objects.filter(org_name=name):
            data["message"] = "该机构已经创建，要修改请返回编辑页面！"
        else:
            data["message"] = "该机构信息尚未创建，创建该机构信息请继续！"
    return JsonResponse(data, safe=False)