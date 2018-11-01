from django.conf.urls import url
from user_management import views

urlpatterns = [
    url(r"^users/", views.users_list),
    url(r"^test/", views.test)
]