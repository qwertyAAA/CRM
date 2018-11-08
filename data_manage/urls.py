from django.conf.urls import url
from data_manage import views

urlpatterns = [
    url(r'^check/',views.check),
    url(r'^add/',views.add),
    url(r'^delete/',views.delete),
    url(r'^edit/(\d+)/',views.edit),
    url(r'^data/(\d+)/',views.checkdata),
]