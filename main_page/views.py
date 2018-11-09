from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from user_management import models
# Create your views here.


def index(request):
    return render(request, "main_page/index.html")


def my_login(request):
    if request.method == "POST":
        ret = {"status": 0, "msg": ""}
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember_me")
        valid_code = request.POST.get("valid_code")
        user = authenticate(username=username, password=password)
        if valid_code.upper() == request.session.get("valid_code", "").upper():
            if user:
                ret["msg"] = "/index/"
                login(request=request, user=user)
                role_permission = []
                qs = models.Permission.objects.filter(group__role__user=user).values_list("role_permission")
                for item in qs:
                    role_permission.append(item[0])
                print(role_permission)
                request.session["role_permission"] = role_permission
                if remember_me == "true":
                    request.session.set_expiry(None)
                else:
                    request.session.set_expiry(0)
            else:
                ret["status"] = 1
                ret["msg"] = "用户名或密码错误"
        else:
            ret["status"] = 1
            ret["msg"] = "验证码错误"
        return JsonResponse(ret)
    return render(request, "main_page/login.html")


def get_valid_img(request):
    # with open("valid_code.png", "rb") as f:
    #     data = f.read()
    # 自己生成一个图片
    from PIL import Image, ImageDraw, ImageFont
    import random

    # 获取随机颜色的函数
    def get_random_color():
        return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

    # 生成一个图片对象
    img_obj = Image.new(
        'RGB',
        (220, 35),
        get_random_color()
    )
    # 在生成的图片上写字符
    # 生成一个图片画笔对象
    draw_obj = ImageDraw.Draw(img_obj)
    # 加载字体文件， 得到一个字体对象
    font_obj = ImageFont.truetype("static/font/msyh.ttc", 28)
    # 开始生成随机字符串并且写到图片上
    tmp_list = []
    for i in range(5):
        u = chr(random.randint(65, 90))  # 生成大写字母
        l = chr(random.randint(97, 122))  # 生成小写字母
        n = str(random.randint(0, 9))  # 生成数字，注意要转换成字符串类型

        tmp = random.choice([u, l, n])
        tmp_list.append(tmp)
        draw_obj.text((20+40*i, 0), tmp, fill=get_random_color(), font=font_obj)

    print("".join(tmp_list))
    print("生成的验证码".center(120, "="))
    # 不能保存到全局变量
    # global VALID_CODE
    # VALID_CODE = "".join(tmp_list)

    # 保存到session
    request.session["valid_code"] = "".join(tmp_list)
    # 加干扰线
    # width = 220  # 图片宽度（防止越界）
    # height = 35
    # for i in range(5):
    #     x1 = random.randint(0, width)
    #     x2 = random.randint(0, width)
    #     y1 = random.randint(0, height)
    #     y2 = random.randint(0, height)
    #     draw_obj.line((x1, y1, x2, y2), fill=get_random_color())
    #
    # # 加干扰点
    # for i in range(40):
    #     draw_obj.point((random.randint(0, width), random.randint(0, height)), fill=get_random_color())
    #     x = random.randint(0, width)
    #     y = random.randint(0, height)
    #     draw_obj.arc((x, y, x+4, y+4), 0, 90, fill=get_random_color())

    # 将生成的图片保存在磁盘上
    # with open("s10.png", "wb") as f:
    #     img_obj.save(f, "png")
    # # 把刚才生成的图片返回给页面
    # with open("s10.png", "rb") as f:
    #     data = f.read()

    # 不需要在硬盘上保存文件，直接在内存中加载就可以
    from io import BytesIO
    io_obj = BytesIO()
    # 将生成的图片数据保存在io对象中
    img_obj.save(io_obj, "png")
    # 从io对象里面取上一步保存的数据
    data = io_obj.getvalue()
    return HttpResponse(data)


def my_logout(request):
    logout(request)
    return redirect("/index/")
