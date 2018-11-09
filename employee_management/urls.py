from django.conf.urls import url
from employee_management import views

urlpatterns = [
     url(r"^main/", views.main),
     url(r"^employee_info/", views.employee_info),
     url(r"^edit_employee/", views.edit_employee),
     url(r"^add_employee/", views.add_employee),
     url(r"^delete_employee/", views.add_employee),
]