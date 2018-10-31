from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# 用户信息表
class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(to=User, to_field="id", verbose_name="用户")
    address = models.CharField(max_length=32, null=True, verbose_name="地址")
    phone_num = models.CharField(max_length=16, null=True, verbose_name="电话")
    image = models.ImageField(upload_to="static/img", default="static/img/default.png", verbose_name="头像")
    gender = models.CharField(max_length=4, verbose_name="性别")
    age = models.IntegerField(null=True, verbose_name="年龄")

    def __str__(self):
        return self.user.username


# 员工信息表
class Staff(models.Model):
    id = models.AutoField(primary_key=True)
    staff_salary = models.FloatField(max_length=32, verbose_name="员工薪资")
    staff_state = models.BooleanField(default=True, verbose_name="员工状态")
    info = models.ManyToManyField(to="UserInfo", to_field="id", verbose_name="员工信息id")


# 部门信息表
class Department(models.Model):
    id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=32, verbose_name="部门名称")
    leader_title = models.CharField(max_length=32, verbose_name="领导职称")
    info = models.ManyToManyField(to="Staff", to_field="id", verbose_name="部门信息id")
