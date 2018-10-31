from django.db import models
from user_management import models as usermodel

# Create your models here.
class Data(models.Model):
    id=models.AutoField(primary_key=True)
    dataname=models.CharField(max_length=50,null=False)#资料名字
    comment=models.FileField(upload_to="filed/", verbose_name="文件")
    createtime=models.DateTimeField(auto_now_add=True)
    updatetime=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(to=usermodel.User,to_field=id)

    def __str__(self):
        return self.dataname

class Category(models.Model):
    nid=models.AutoField(primary_key=True)
    title=models.CharField(max_length=30)#分类标题
    data=models.ForeignKey(to='Data',to_field='id')

    def __str__(self):
        return self.title
