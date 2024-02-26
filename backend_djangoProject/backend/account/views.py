import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

from ..account.models import User, ClothList, MyLove

# Create your views here.

from django.http import JsonResponse


# 登录
def login(request):
    if request.method == "GET":
        return JsonResponse({"message": "Please use POST method to login."})

    data = json.loads(request.body)
    name = data.get("name")
    password = data.get("password")
    role = data.get("role")
    users = User.objects.filter(name=name, password=password, role=role)
    if users.exists():
        return JsonResponse({"message": "登录成功"})
    else:
        return JsonResponse({"message": "用户名或密码错误"})


# 退出登录
def logout(request):
    return HttpResponse("退出登录")


# 注册
def register(request):
    if request.method == "GET":
        return JsonResponse({"message": "Please use POST method to register."})

    data = json.loads(request.body)
    name = data.get("name")
    if not name:  # 检查'name'字段是否存在或为空
        return JsonResponse({"message": "用户名不能为空"})
    password = data.get("password")
    role = data.get("role")

    if User.objects.filter(name=name, password=password, role=role).exists():
        return JsonResponse({"message": "该用户已存在"})

    user = User.objects.create(name=name, password=password, role=role)
    return JsonResponse({"message": "注册成功", "user_id": user.id})


# 首页
def index(request):
    return JsonResponse({})


# 服装列表
def list(request):
    if request.method == "GET":
        clothes = ClothList.objects.all()
        data = []
        for item in clothes:
            data.append(
                {"name": item.item_name, "type": item.style, "img": item.pic, "real_sales": item.real_sales,
                 "isLiked": item.isLiked, "procity": item.procity, "applicable_age": item.applicable_age,
                 "fabric": item.fabric, "season": item.season, "price": item.price}
            )
        return JsonResponse(data, safe=False)
    cloth = ClothList.objects.all()
    data = []
    for item in cloth:
        data.append({"name": item.item_name, "type": item.style, "img": item.pic, "real_sales": item.real_sales,
                     "isLiked": item.isLiked, "procity": item.procity, "applicable_age": item.applicable_age,
                     "fabric": item.fabric, "season": item.season, "price":item.price}
                    )

    return JsonResponse(data, safe=False)

        # 我的喜欢

def mylove(request):
    if request.method == "GET":
        clothes = MyLove.objects.all()
        data = []
        for item in clothes:
            data.append({"name": item.item_name, "type": item.style, "img": item.pic, "real_sales": item.real_sales,
                         "isLiked": item.isLiked, "procity": item.procity, "applicable_age": item.applicable_age,
                         "fabric": item.fabric, "season": item.season, "price":item.price}
                        )
        return JsonResponse(data, safe=False)
    if request.method == "POST":
        data = json.loads(request.body)
        name = data.get("name")
        type = data.get("type")
        img = data.get("img")
        isLiked = data.get("isLiked")
        real_sales = data.get("real_sales")
        procity = data.get("procity")
        applicable_age = data.get("applicable_age")
        fabric = data.get("fabric")
        season = data.get("season")
        price = data.get("price")
        ClothList.objects.all().filter(item_name=name, style=type, pic=img,
                                       real_sales=real_sales,procity=procity,applicable_age=applicable_age,
                                       fabric=fabric,season=season,price=price).update(isLiked=isLiked)
        clothes = ClothList.objects.all().filter(item_name=name, style=type, pic=img,
                                                 real_sales=real_sales, procity=procity,
                                                 applicable_age=applicable_age,
                                                 fabric=fabric, season=season, price=price,
                                                 isLiked="true")

        for cloth in clothes:
            MyLove.objects.create(item_name=cloth.item_name, style=cloth.style, pic=cloth.pic,
                                  real_sales=cloth.real_sales, procity=cloth.procity,
                                  applicable_age=cloth.applicable_age,
                                  fabric=cloth.fabric, season=cloth.season, price=cloth.price,
                                  isLiked=cloth.isLiked)

        return JsonResponse({"message": "添加到我的喜欢成功"})
    if request.method == "DELETE":
        data = json.loads(request.body)
        name = data.get("name")
        type = data.get("type")
        img = data.get("img")
        isLiked = data.get("isLiked")
        real_sales = data.get("real_sales")
        procity = data.get("procity")
        applicable_age = data.get("applicable_age")
        fabric = data.get("fabric")
        season = data.get("season")
        price = data.get("price")
        MyLove.objects.all().filter(item_name=name, style=type, pic=img,
                                    real_sales=real_sales, procity=procity,
                                    applicable_age=applicable_age,
                                    fabric=fabric, season=season, price=price,
                                    isLiked="true").delete()
        ClothList.objects.all().filter(item_name=name, style=type, pic=img,
                                       real_sales=real_sales, procity=procity,
                                       applicable_age=applicable_age,
                                       fabric=fabric, season=season, price=price
                                       ).update(isLiked="false")
        return JsonResponse({"message": "我不喜欢了~删除成功"})
