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


# 角色表
class Role(models.Model):
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=32, verbose_name="角色名")
    user = models.ManyToManyField(
        to=User,
        verbose_name="用户"
    )


# 权限表
class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    permission_name = models.CharField(max_length=32)
    info = models.OneToOneField(to="PermissionInfo", to_field="id", verbose_name="权限信息")
    role = models.ManyToManyField(
        to="Role",
        verbose_name="角色"
    )


# 权限信息表
class PermissionInfo(models.Model):
    id = models.AutoField(primary_key=True)
    update = models.BooleanField(default=False, verbose_name="更新权限")
    delete = models.BooleanField(default=False, verbose_name="删除权限")
    change = models.BooleanField(default=False, verbose_name="修改权限")
    select = models.BooleanField(default=True, verbose_name="查看权限")


