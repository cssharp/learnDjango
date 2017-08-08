#coding:utf-8
from django.db import models

# Create your models here.
class Member(models.Model):
    class Meta:
        verbose_name = '用户' #提供了一个更容易让人阅读的名称
        verbose_name_plural = '用户列表' #复数形式
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
        verbose_name_plural = '订单列表'
    orderId = models.AutoField(primary_key=True)
    userName = models.CharField("用户名", max_length=100, null=True, blank=True)
    mobile = models.CharField("手机号", max_length=11, null=False, blank=False)
    url = models.CharField("网址", max_length=1000, null=True, blank=True)
    desc = models.TextField("备注", null=True, blank=True)
    price = models.IntegerField("价格美元($)", null=True, blank=True)
    isReceiveOrder = models.BooleanField("是否接单", default=False)
    isPurchased = models.BooleanField("是否采购", default=False)
    isConfirmReceipt = models.BooleanField("是否收货", default=False)
    createTime = models.DateTimeField("创建时间", auto_now_add=True)
    updateTime = models.DateTimeField("更新时间", auto_now=True)

    def __unicode__(self):
        return self.mobile


class Item(models.Model):
    class Meta:
        verbose_name = '商品'
        verbose_name_plural = '商品列表'
    itemId = models.AutoField(primary_key=True)
    itemName = models.CharField("商品名称", max_length=100, null=False, blank=False)
    itemPics = models.CharField("商品图片", max_length=500, null=False, blank=False)
    itemUSDPrice = models.IntegerField("价格美元($)", null=True, blank=True)
    itemCnPrice = models.IntegerField("价格人民币(¥)", null=True, blank=True)
    itemDesc = models.TextField("商品描述", max_length=500, null=False, blank=False)
    itemWeight = models.IntegerField("重量（磅）", null=False, blank=False)
    itemSourceUrl = models.CharField("商品url", max_length=300, null=True, blank=True)

    def __unicode__(self):
        return self.itemName
