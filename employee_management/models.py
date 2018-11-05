from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# 员工信息表
class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=32, verbose_name="员工姓名")
    staff_salary = models.FloatField(max_length=32, verbose_name="员工薪资")
    staff_state = models.BooleanField(default=True, verbose_name="员工状态")
    staff_job = models.CharField(max_length=32, verbose_name="职位名称")
    staff_job_level = models.CharField(max_length=32, verbose_name="职务级别")
    user = models.OneToOneField(to=User, to_field="id", verbose_name="员工信息id")
    department = models.ManyToManyField(to="Department")


# 部门信息表
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=32, verbose_name="部门名称")
    leader_title = models.CharField(max_length=32, verbose_name="领导职称")
