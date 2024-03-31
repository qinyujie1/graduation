from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(verbose_name="用户名", max_length=20)
    password = models.CharField(verbose_name="密码", validators=[MinLengthValidator(6)], max_length=20)
    role = models.CharField(verbose_name="角色", max_length=6)


class ClothList(models.Model):
    id= models.BigIntegerField(verbose_name="id", primary_key=True)
    item_name = models.CharField(verbose_name="服装名字", max_length=200)
    style = models.CharField(verbose_name="服装类型", max_length=20)
    price = models.CharField(verbose_name="服装价格", max_length=50)
    real_sales = models.CharField(verbose_name="购买人数", max_length=50)
    pic = models.CharField(verbose_name="服装图片", max_length=1000)
    procity = models.CharField(verbose_name="生产地", max_length=50)
    applicable_age = models.CharField(verbose_name="适合年龄", max_length=50)
    fabric = models.CharField(verbose_name="材质", max_length=200)
    season = models.CharField(verbose_name="适合季节", max_length=200)
    isLiked = models.CharField(verbose_name="喜欢状态", default="false", max_length=20)


class MyLove(models.Model):
    item_name = models.CharField(verbose_name="服装名字", max_length=200)
    style = models.CharField(verbose_name="服装类型", max_length=20)
    price = models.CharField(verbose_name="服装价格", max_length=50)
    real_sales = models.CharField(verbose_name="购买人数", max_length=50)
    pic = models.CharField(verbose_name="服装图片", max_length=1000)
    procity = models.CharField(verbose_name="生产地", max_length=50)
    applicable_age = models.CharField(verbose_name="适合年龄", max_length=50)
    fabric = models.CharField(verbose_name="材质", max_length=200)
    season = models.CharField(verbose_name="适合季节", max_length=200)
    isLiked = models.CharField(verbose_name="喜欢状态", default="true", max_length=20)
