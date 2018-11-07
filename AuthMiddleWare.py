from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect


class CheckAuth(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        current_permission = request.session.get("permission")["role_permission"]
        current_permission.append(request.session.get("permission")["data_permission"])
        if request.path in current_permission:
            return
        else:
            return redirect("/index/")
