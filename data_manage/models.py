from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Data(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="编号")
    data_name = models.CharField(max_length=50, null=False,verbose_name="资料名字")  # 资料名字
    comment = models.FileField(upload_to="filed/", verbose_name="文件")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now_add=True,verbose_name="更新时间")
    user = models.ForeignKey(to=User,verbose_name="发布者")
    category = models.ForeignKey(to='Category', to_field='id',verbose_name="资料分类")

    def __str__(self):
        return self.data_name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30,verbose_name='分类名')  # 分类标题

    def __str__(self):
        return self.title
