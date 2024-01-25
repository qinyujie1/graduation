from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(verbose_name="用户名",max_length=20)
    password = models.CharField(verbose_name="密码",validators=[MinLengthValidator(6)], max_length=20)
    role = models.CharField(verbose_name="角色",max_length=6)
    class Meta:
        app_label = '用户类'
class ClothList(models.Model):
    name = models.CharField(verbose_name="服装名字",max_length=50)
    type = models.CharField(verbose_name="服装类型",max_length=20)
    detail = models.CharField(verbose_name="服装详情",max_length=200)
    img =models.CharField(verbose_name="服装图片",max_length=1000)
    isLiked = models.CharField(verbose_name="喜欢状态",default="false",max_length=20)
class MyLove(models.Model):
    name = models.CharField(verbose_name="服装名字", max_length=50)
    type = models.CharField(verbose_name="服装类型", max_length=20)
    detail = models.CharField(verbose_name="服装详情", max_length=200)
    img = models.CharField(verbose_name="服装图片", max_length=1000)
    isLiked = models.CharField(verbose_name="喜欢状态",default="true", max_length=20)