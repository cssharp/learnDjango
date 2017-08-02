#coding:utf-8
from django.db import models

# Create your models here.
class Member(models.Model):
    class Meta:
        verbose_name = '用户' #提供了一个更容易让人阅读的名称
        verbose_name_plural = '用户' #复数形式
    memberId = models.AutoField(primary_key=True) #models.IntegerField(auto_created=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50, null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)
    isDeleted = models.BooleanField()
    isEnabled = models.BooleanField()
    createTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)
    myCode = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.userName


class Order(models.Model):
    class Meta:
        verbose_name = '订单'
        verbose_name_plural = '订单'
    orderId = models.AutoField(primary_key=True)
    userName = models.CharField("用户名", max_length=100, null=True, blank=True)
    mobile = models.CharField("手机号", max_length=11, null=False, blank=False)
    url = models.CharField("网址", max_length=1000, null=True, blank=True)
    desc = models.TextField("备注", null=True, blank=True)
    isReceiveOrder = models.BooleanField("是否接单")
    isPurchased = models.BooleanField("是否采购")
    isConfirmReceipt = models.BooleanField("是否收货")
    createTime = models.DateTimeField("创建时间", auto_now_add=True)
    updateTime = models.DateTimeField("更新时间", auto_now=True)

    def __unicode__(self):
        return self.mobile


