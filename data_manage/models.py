from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Data(models.Model):
    id = models.AutoField(primary_key=True)
    data_name = models.CharField(max_length=50, null=False)  # 资料名字
    comment = models.FileField(upload_to="filed/", verbose_name="文件")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(to=User)
    data = models.ForeignKey(to='Category', to_field='id')

    def __str__(self):
        return self.data_name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)  # 分类标题

    def __str__(self):
        return self.title
