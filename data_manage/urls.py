from django.conf.urls import url
from data_manage import views

urlpatterns = [
    url(r'^check/',views.check),
]