from django.conf.urls import url
from organization import views

urlpatterns = [
    url(r'^$', views.organ_list),
]