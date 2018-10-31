from django.db import models

# Create your models here.
class Data(models.Model):
    id=models.AutoField(primary_key=True)
    dataname=models.CharField(max_length=50,null=False)#资料名字
    comment=models.FileField(upload_to="filed/", verbose_name="文件")
    createtime=models.DateTimeField(auto_now_add=True)
    updatetime=models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=30)#分类标题
    data=models.ForeignKey(to='Data',to_field='id')
