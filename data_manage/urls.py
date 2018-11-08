from django.conf.urls import url
from data_manage import views

urlpatterns = [
    url(r'^check/',views.check),
    url(r'^add/',views.add),
    url(r'^delete/',views.delete),
    url(r'^edit/(\d+)/',views.edit),
    url(r'^data/(\d+)/',views.checkdata),
    url(r'^check_category/',views.cheak_category),
    url(r'^add_category/',views.add_category),
    url(r'^delete_category/',views.delete_category),
    url(r'^edit_category/(\d+)/',views.edit_category),
]