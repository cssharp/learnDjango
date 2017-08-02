#coding:utf-8
from django.db import models

# Create your models here.
class Member(models.Model):
    class Meta:
        verbose_name = '用户' #提供了一个更容易让人阅读的名称
        verbose_name_plural = '用户' #复数形式
    memberId = models.AutoField(primary_key=True) #models.IntegerField(auto_created=True)
    email = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    score = models.IntegerField()
    isDeleted = models.BooleanField()
    isEnabled = models.BooleanField()
    createTime = models.DateTimeField()
    myCode = models.CharField(max_length=50)

    def __unicode__(self):
        return self.userName
