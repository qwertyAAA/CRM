from django.db import models


# Create your models here.

# 机构信息表
class Organ(models.Model):
    # 基本信息
    org_name = models.CharField(max_length=50, blank=False, null=False, verbose_name="机构名称")
    org_address = models.CharField(max_length=100, blank=False, null=False, verbose_name="机构地址")
    linkman = models.OneToOneField("Linkman", blank=False, null=False, verbose_name="联系人")
    mobile = models.IntegerField(blank=False, null=False, verbose_name="手机")
    tel = models.IntegerField(blank=False, null=False, verbose_name="电话")
    country = models.CharField(max_length=20, blank=True, null=True, verbose_name="国家")
    province = models.CharField(max_length=20, blank=False, null=False, verbose_name="省份")
    city = models.CharField(max_length=20, blank=False, null=False, verbose_name="城市")
    postcode = models.CharField(max_length=6, blank=True, null=True, verbose_name="邮编")
    site = models.CharField(max_length=50, blank=True, null=True, verbose_name="网站")
    industry = models.CharField(max_length=10, blank=False, null=False, verbose_name="行业类别")
    area_level = models.CharField(max_length=10, blank=False, null=False, verbose_name="区域等级")

    # 其他信息
    agent = models.CharField(max_length=20, blank=False, null=False, verbose_name="经办人")
    pur_level = models.CharField(max_length=10, blank=True, null=True, verbose_name="采购级别")
    pur_way = models.CharField(max_length=10, blank=True, null=True, verbose_name="采购途径")
    distribution = models.BooleanField(blank=False, null=False, verbose_name="分配情况")
    check_status = models.CharField(max_length=10, blank=False, null=False, verbose_name="审核状态")
    org_category = models.CharField(max_length=10, blank=False, null=False, verbose_name="机构类型")
    follow_status = models.CharField(max_length=10, blank=False, null=False, verbose_name="跟进状态")
    remark = models.TextField(max_length=200, blank=True, null=True, verbose_name="备注信息")
    tag = models.CharField(max_length=10, blank=True, null=True, verbose_name="标签")

    def __str__(self):
        return self.org_name


# 联系人信息表
class Linkman(models.Model):
    name = models.CharField(max_length=10, blank=False, null=False, verbose_name="姓名")
    gender = models.BooleanField(blank=False, null=False, verbose_name="性别")
    duty = models.CharField(max_length=10, blank=False, null=False, verbose_name="职务")
    phone = models.IntegerField(blank=False, null=False, verbose_name="手机")
    email = models.EmailField(blank=False, null=False, verbose_name="邮箱")
    QQ = models.IntegerField(blank=False, null=False, verbose_name="QQ")
    address = models.CharField(max_length=50, blank=True, null=True, verbose_name="地址")
    link_important = models.CharField(max_length=10, blank=False, null=False, verbose_name="重要等级")
    following = models.CharField(max_length=10, blank=False, null=False, verbose_name="跟进状态")
    link_agent = models.CharField(max_length=20, blank=False, null=False, verbose_name="经办人")
    is_accept = models.BooleanField(blank=False, null=False, verbose_name="是否认可")
    remark = models.TextField(max_length=200, blank=True, null=True, verbose_name="备注")

    def __str__(self):
        return "%s--%s" % (self.name, self.organ.org_name)
