import json
import re

from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render, redirect
from collections import defaultdict

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from ..account.models import User, ClothList, MyLove

# Create your views here.

from django.http import JsonResponse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity


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
def list1(request):
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
                     "fabric": item.fabric, "season": item.season, "price": item.price}
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
                         "fabric": item.fabric, "season": item.season, "price": item.price}
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
                                       real_sales=real_sales, procity=procity, applicable_age=applicable_age,
                                       fabric=fabric, season=season, price=price).update(isLiked=isLiked)
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


def recommend(request):
    if request.method == 'POST':
        user_clothes = MyLove.objects.filter(isLiked=True)
        all_clothes = ClothList.objects.all()

        # 提取用户喜欢的服装特征
        user_features = []
        for cloth in user_clothes:
            features = [cloth.style, cloth.price, cloth.real_sales, cloth.procity, cloth.applicable_age, cloth.fabric,
                        cloth.season]
            feature_desc = " ".join(str(feature) for feature in features if feature)
            if feature_desc:
                user_features.append(feature_desc)

        if not user_features:
            return JsonResponse({"error": "No complete features extracted from user's liked clothes."}, status=400)

        # 使用TF-IDF向量化用户喜欢的服装特征
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(user_features)

        # 计算用户喜欢的服装之间的相似度
        user_similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)

        # 计算所有服装和用户喜欢的服装之间的相似度
        all_features = []
        for cloth in all_clothes:
            features = [cloth.style, cloth.price, cloth.real_sales, cloth.procity, cloth.applicable_age, cloth.fabric,
                        cloth.season]
            feature_desc = " ".join(str(feature) for feature in features if feature)
            if feature_desc:
                all_features.append(feature_desc)

        all_tfidf_matrix = tfidf.transform(all_features)
        all_user_similarity = cosine_similarity(all_tfidf_matrix, tfidf_matrix)

        # 根据相似度推荐服装
        recommended_clothes = []
        for idx, cloth in enumerate(all_clothes):
            if idx < len(all_user_similarity):
                similarity_scores = all_user_similarity[idx]
                avg_similarity = sum(similarity_scores) / len(similarity_scores)
                recommended_clothes.append((cloth, avg_similarity))

        # 按相似度降序排序推荐服装
        recommended_clothes.sort(key=lambda x: x[1], reverse=True)
        recommended_clothes = [cloth[0] for cloth in recommended_clothes]

        # 返回推荐的服装数据给前端
        # 这里可以根据需要将推荐的服装数据格式化后返回给前端

        # 将 ClothList 对象转换为字典，并包含相似度信息和相似度平均值
        recommended_clothes_data = []
        for cloth, similarity in zip(recommended_clothes, all_user_similarity):
            average_similarity = sum(similarity) / len(similarity)  # 计算相似度平均值
            cloth_data = {
                'id': cloth.id,
                "item_name": cloth.item_name,
                "pic": cloth.pic,
                'style': cloth.style,
                'price': cloth.price,
                'real_sales': cloth.real_sales,
                'procity': cloth.procity,
                'applicable_age': cloth.applicable_age,
                'fabric': cloth.fabric,
                'season': cloth.season,
                'similarity': similarity.tolist(),  # 将相似度转换为列表
                'average_similarity': average_similarity  # 添加相似度平均值
            }
            recommended_clothes_data.append(cloth_data)

        # 根据相似度平均值对服装数据进行排序
        recommended_clothes_data = sorted(recommended_clothes_data, key=lambda x: x['average_similarity'], reverse=True)

        return JsonResponse(recommended_clothes_data, safe=False)


# 总览页
def dashboards(request):
    if request.method == 'GET':
        cloth_items = ClothList.objects.all()

        # 使用 defaultdict 初始化一个字典，用于存储每种风格的购买人数总和
        style_sales = defaultdict(int)

        for item in cloth_items:
            # 提取购买人数中的数字部分
            sales = re.findall(r'\d+', item.real_sales)
            if sales:
                # 将提取的数字部分转换为整数并加入对应风格的购买人数总和中
                if item.style is not None:
                    style_sales[item.style] += int(sales[0])

        series_data = []
        # 按照销售人数降序排序并选择前十个风格
        sorted_styles = sorted(style_sales.items(), key=lambda x: x[1], reverse=True)[:10]

        # 创建 x 轴数据列表，选择前 10 个风格作为 x 轴数据点
        x_axis_data = [style for style, _ in sorted_styles]

        # 构建 series_data 列表
        for style, total_sales in sorted_styles:
            data_list = []
            for key in x_axis_data:
                if key == style:
                    data_list.append(total_sales)
                else:
                    data_list.append(0)

            series_data.append({
                "name": style,
                "type": "bar",
                "stack": "Total",
                "data": data_list,
                "label": {
                    "show": True,  # 显示标签
                    "position": "top",  # 标签位置
                    "formatter": "{c}"  # 显示数据值
                },

            })

        option = {
            "title": {"text": "Top 10 Clothing Sales by Style"},
            "xAxis": [{"type": "category", "data": x_axis_data}],
            "yAxis": [{"type": "value"}],
            "series": series_data,
        }

        return JsonResponse(option, safe=False)


# 饼图
def dashboards1(request):
    if request.method == 'GET':
        cloth_items = ClothList.objects.all()

        # 使用 defaultdict 初始化一个字典，用于统计每种风格的数量
        style_count = defaultdict(int)

        for item in cloth_items:
            if item.style is not None:
                style_count[item.style] += 1

        # 准备饼图所需的数据
        data = []
        for style, count in style_count.items():
            data.append({"name": style, "value": count})

        option = {

            "series": [{
                "name": "Styles",
                "type": "pie",
                "radius": "50%",
                "data": data,
                "label": {
                    "show": True,
                    "formatter": "{b}: {c} ({d}%)"
                }
            }]
        }

        return JsonResponse(option, safe=False)


# admin销售地销售人数
def admin_login_dashbords(request):
    if request.method == 'GET':
        cloth_items = ClothList.objects.all()

        # 使用 defaultdict 初始化一个字典，用于存储每个地区的购买人数总和
        procity_sales = defaultdict(int)

        for item in cloth_items:
            procity = item.procity.split(' ')[0].strip()
            sales = re.findall(r'\d+', item.real_sales)
            if sales:
                procity_sales[procity] += int(sales[0])

        # 构建横坐标和纵坐标数据
        x_axis_data = list(procity_sales.keys())  # 生产地数据作为横坐标
        y_axis_data = [procity_sales[procity] for procity in x_axis_data]  # 对应的销售人数作为纵坐标

        # 构建返回给前端的数据结构
        data = {
            'xAxis': x_axis_data,
            'yAxis': y_axis_data,
            'series': [{
                'data': y_axis_data,
                'type': 'bar'
            }]
        }

        return JsonResponse(data, safe=False)


# admin销售总额
def admin_login_dashbords1(request):
    if request.method == 'GET':
        cloth_items = ClothList.objects.all()
        total_sales = 0

        for item in cloth_items:
            price = item.price
            real_sales = re.findall(r'\d+', item.real_sales)
            real_sales = int(real_sales[0]) if real_sales else 0
            sales = int(price) * int(real_sales)
            total_sales += sales

        data = {
            'total_sales': total_sales
        }

        return JsonResponse(data, safe=False)


# admin销售总人数
def admin_login_dashbords2(request):
    if request.method == 'GET':
        cloth_items = ClothList.objects.all()
        total_sales = 0

        for item in cloth_items:
            real_sales = re.findall(r'\d+', item.real_sales)
            real_sales = int(real_sales[0]) if real_sales else 0
            sales = int(real_sales)
            total_sales += sales

        data = {
            'total_people': total_sales
        }

        return JsonResponse(data, safe=False)


# admin服装总数量
def admin_login_dashbords3(request):
    if request.method == 'GET':
        cloth_items = ClothList.objects.all()
        total_cloth = len(cloth_items)

        data = {
            'total_people': total_cloth
        }

        return JsonResponse(data, safe=False)


# 用户管理
@csrf_exempt
@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def user_manage(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_list = []
        for user in users:
            user_dict = {
                'id': user.id,
                'name': user.name,
                'password': user.password,
                'role': user.role
            }
            users_list.append(user_dict)
        return JsonResponse(users_list, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        password = data.get('password')
        role = data.get('role')
        new_user = User(name=name, password=password, role=role)
        new_user.save()
        return JsonResponse({'message': 'User created successfully'})


@csrf_exempt
@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def user_manage1(request, userId):
    if request.method == 'PUT':
        data = json.loads(request.body)
        print(data)
        user = User.objects.get(id=userId)

        # 检查密码字段是否为空
        if 'password' in data and data['password'] is not None:
            user.password = data.get('password')

        user.name = data.get('name')
        user.role = data.get('role')
        user.save()
        return JsonResponse({'message': 'User updated successfully'},safe=False)

    elif request.method == 'DELETE':
        user = User.objects.get(id=userId)
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'})
    elif request.method == 'GET':
        if request.method == 'GET':
            try:
                user = User.objects.get(id=userId)
                user_data = {
                    'id': user.id,
                    'name': user.name,
                    'role': user.role,
                    'password': user.password
                }
                return JsonResponse(user_data)
            except User.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)



