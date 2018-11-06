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
from django.conf.urls import url, include
from main_page import views as mpv
from data_manage import urls as data_manage_urls
from employee_management import urls as employee_management_urls

urlpatterns = [
    url(r"^$", mpv.index),
    url(r"^index/", mpv.index),
    url(r"^login/", mpv.login),
    url(r'^data_manage/', include(data_manage_urls)),
    url(r"^user_management/", include("user_management.urls")),
    url(r"^employee_management/", include(employee_management_urls)),

]
