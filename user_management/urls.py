"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from user_management import views

urlpatterns = [
    url(r"^auth/", views.auth),
    url(r"^change_pwd/", views.change_pwd),
    url(r"^edit_user/", views.edit_user),
    url(r"^search_user/", views.search_user),
    url(r"^user_info/", views.user_info),
    url(r"^role_permission/", views.role_permission),
    url(r"^edit_role/", views.edit_role),
]
