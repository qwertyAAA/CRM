from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render


class CheckLogin(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        white_list = ["/", "/login/", "/register/", "/index/", "/get_valid_img.png/", "/logout/"]
        if request.path in white_list or "admin" in request.path:
            return
        if request.user.is_anonymous:
            return render(request, "main_page/login.html")