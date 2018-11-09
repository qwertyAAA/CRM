from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class CheckAuth(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        white_list = ["/", "/login/", "/index/", "/get_valid_img.png/", "/logout/", "/user_management/edit_user/"]
        if request.path_info in white_list:
            return
        current_permission = request.session.get("role_permission")
        print(current_permission)
        print(request.path_info)
        user_url = request.path_info.split("/")[-2]
        user_url += "/"
        if user_url not in current_permission:
            return HttpResponse("您没有权限！")
