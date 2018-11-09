from django.conf.urls import url
from organization import views

urlpatterns = [
    url(r'^$', views.organ_view),
    url(r'^view/$', views.organ_view),
    url(r'^add/$', views.organ_add),
    url(r'^edit/(\d+)/$', views.organ_edit),
    url(r'^detail/(\d+)/$', views.organ_detail),
    url(r'^search/$', views.organ_search),
    url(r'^linkman_list/$', views.linkman_view),
    url(r'^linkman_add/$', views.linkman_add),
    url(r'^linkman_edit/(\d+)/$', views.linkman_edit),
    url(r'^linkman_detail/(\d+)/$', views.linkman_detail),
    url(r'^linkman_search/$', views.linkman_search),
    url(r'^org_name_check/$', views.org_name_check),
    url(r'^org_name_check2/$', views.org_name_check2),
    url(r'^linkman_delete/(\d+)/$', views.linkman_delete),
    url(r'^delete/(\d+)/$', views.organ_delete),
    url(r'^organ_batch/$', views.organ_batch),
    url(r'^linkman_batch/$', views.linkman_batch),
]
