import base64
import json
import re
from io import BytesIO

from django.contrib.auth import logout
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render, redirect
from collections import defaultdict, Counter

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from matplotlib import pyplot as plt
from wordcloud import WordCloud

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
def logout1(request):
    if request.method == "GET":
        logout(request)
        return JsonResponse({"message": "您已成功退出登录"})


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
                {"id": item.id, "name": item.item_name, "type": item.style, "img": item.pic,
                 "real_sales": item.real_sales,
                 "isLiked": item.isLiked, "procity": item.procity, "applicable_age": item.applicable_age,
                 "fabric": item.fabric, "season": item.season, "price": item.price}
            )
        return JsonResponse(data, safe=False)
    cloth = ClothList.objects.all()
    data = []
    for item in cloth:
        data.append(
            {"id": item.id, "name": item.item_name, "type": item.style, "img": item.pic, "real_sales": item.real_sales,
             "isLiked": item.isLiked, "procity": item.procity, "applicable_age": item.applicable_age,
             "fabric": item.fabric, "season": item.season, "price": item.price}
        )

    return JsonResponse(data, safe=False)


# 详情
# 单个服装详情
def detail(request, nid):
    if request.method == "POST":
        try:
            cloth = ClothList.objects.get(id=nid)
            data = {
                "id": cloth.id,
                "name": cloth.item_name,
                "type": cloth.style,
                "img": cloth.pic,
                "real_sales": cloth.real_sales,
                "isLiked": cloth.isLiked,
                "procity": cloth.procity,
                "applicable_age": cloth.applicable_age,
                "fabric": cloth.fabric,
                "season": cloth.season,
                "price": cloth.price
            }
            return JsonResponse(data)
        except ClothList.DoesNotExist:
            return JsonResponse({"error": "Cloth not found"}, status=404)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)


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

        # 仅保留推荐度前十的服装数据
        recommended_clothes = recommended_clothes[:10]

        # 返回推荐度前十的服装数据给前端
        recommended_clothes_data = []
        for cloth, similarity in recommended_clothes:
            similarity = [similarity]  # 将相似度转换为包含单个值的列表
            average_similarity = similarity[0]  # 取出单个相似度值
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
                'similarity': similarity,  # 将相似度转换为列表
                'average_similarity': average_similarity  # 添加相似度平均值
            }
            recommended_clothes_data.append(cloth_data)

        return JsonResponse(recommended_clothes_data, safe=False)


# 总览页 销售人数排行前五

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
        # 按照销售人数降序排序并选择前五个风格
        sorted_styles = sorted(style_sales.items(), key=lambda x: x[1], reverse=True)[:5]

        # 创建 y 轴数据列表，选择前 5 个风格作为 y 轴数据点
        y_axis_data = [style for style, _ in sorted_styles]

        # 获取最大销售人数
        max_sales = max([total_sales for _, total_sales in sorted_styles])

        # 构建 series_data 列表
        data_list = []
        for style, total_sales in sorted_styles:
            data = []
            for key in y_axis_data:
                if key == style:
                    data.append(total_sales)
                else:
                    data.append(0)
            data_list.append(data)

            series_data.append({
                "name": style,
                "type": "bar",
                "barWidth": 10,
                "barGap": "-70%",
                "data": data_list[-1],  # 使用最后一个 data_list 中的数据
                "itemStyle": {
                    "normal": {
                        "barBorderRadius": 30,
                        "color": {
                            "type": "linear",
                            "x": 0,
                            "y": 0,
                            "x2": 1,
                            "y2": 0,
                            "colorStops": [
                                {
                                    "offset": 0,
                                    "color": "rgb(57,89,255,1)"
                                },
                                {
                                    "offset": 1,
                                    "color": "rgb(46,200,207,1)"
                                }
                            ]
                        }
                    }
                },
            })

        option = {
            "backgroundColor": "#003366",
            "grid": {
                "left": "2%",
                "right": "2%",
                "bottom": "0%",
                "top": "2%",
                "containLabel": True,
            },
            "tooltip": {
                "trigger": "axis",
                "axisPointer": {
                    "type": "none",
                },
                "formatter": "function (params) { return params[0].name + ' : ' + params[0].value; }",
            },
            "xAxis": {
                "show": False,
                "type": "value",
            },
            "yAxis": [
                {
                    "type": "category",
                    "position": "left",  # 将第一个 y 轴设置在左侧
                    "inverse": True,
                    "axisLabel": {
                        "show": True,
                        "textStyle": {
                            "color": "#fff",
                        },
                    },
                    "splitLine": {
                        "show": False,
                    },
                    "axisTick": {
                        "show": False,
                    },
                    "axisLine": {
                        "show": False,
                    },
                    "data": y_axis_data,
                },
                {
                    "type": "category",
                    "position": "insideRight",  # 将第二个 y 轴设置在柱状图内部右侧
                    "inverse": True,
                    "axisTick": "none",
                    "axisLine": "none",
                    "show": True,
                    "axisLabel": {
                        "inside": "true",
                        "textStyle": {
                            "color": "#ffffff",
                            "fontSize": "12",
                        },
                        "z": 100,  # 调整标签的层叠顺序，数值越大显示在上层
                    },
                    "data": [total_sales for _, total_sales in sorted_styles],
                },
            ],
            "series": series_data,

        }

        return JsonResponse(option, safe=False)


# 饼图 每种风格数量
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


# admin生产地销售人数
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
            }],
            'title': {
                'text': '各生产地销售人数',
                'subtext': 'Number of sales by production location'
            },
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
            'total_cloth': total_cloth
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
        return JsonResponse({'message': 'User updated successfully'}, safe=False)

    elif request.method == 'DELETE':
        user = User.objects.get(id=userId)
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'})
    elif request.method == 'GET':
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


# 库存管理
@csrf_exempt
@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def inventory_management(request):
    if request.method == 'GET':
        clothes = ClothList.objects.all()

        # 分页
        paginator = Paginator(clothes, 20)  # 每页最多20条数据
        page = request.GET.get('page')
        try:
            cloth_list = paginator.page(page)
        except PageNotAnInteger:
            cloth_list = paginator.page(1)
        except EmptyPage:
            cloth_list = paginator.page(paginator.num_pages)

        serialized_cloth_list = []
        for cloth in cloth_list:
            cloth_dict = {
                "id": cloth.id,
                "name": cloth.item_name,
                "type": cloth.style,
                "img": cloth.pic,
                "real_sales": cloth.real_sales,
                "isLiked": cloth.isLiked,
                "procity": cloth.procity,
                "applicable_age": cloth.applicable_age,
                "fabric": cloth.fabric,
                "season": cloth.season,
                "price": cloth.price
            }
            serialized_cloth_list.append(cloth_dict)
        return JsonResponse({
            'results': serialized_cloth_list,
            'total_pages': paginator.num_pages
        }, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        id = data.get('id')
        name = data.get('name')
        if data.get('type'):
            type = data.get('type')
        else:
            type = None
        if data.get('img'):
            img = data.get('img')
        else:
            img = 'https://g-search3.alicdn.com/img/bao/uploaded/i4/i1/709048633/O1CN015QjYca2Ddy7uH259j_!!709048633.jpg'

        if data.get('real_sales'):
            real_sales = data.get('real_sales')
        else:
            real_sales = None
        isLiked = data.get('isLiked')
        if data.get('procity'):
            procity = data.get('procity')
        else:
            procity = None
        if data.get('applicable_age'):
            applicable_age = data.get('applicable_age')
        else:
            applicable_age = None
        if data.get('fabric'):
            fabric = data.get('fabric')
        else:
            fabric = None
        if data.get('season'):
            season = data.get('season')
        else:
            season = None
        if data.get('price'):
            price = data.get('price')
        else:
            price = None

        new_cloth = ClothList(id=id, item_name=name, style=type, pic=img, real_sales=real_sales, isLiked=isLiked,
                              procity=procity, applicable_age=applicable_age,
                              fabric=fabric, season=season, price=price)

        new_cloth.save()
        return JsonResponse({'message': 'Cloth created successfully'})


@csrf_exempt
@require_http_methods(["GET", "POST", "PUT", "DELETE"])
def inventory_management1(request, clothId):
    if request.method == 'PUT':
        data = json.loads(request.body)
        print(data)
        cloth = ClothList.objects.get(id=clothId)

        # 检查密码字段是否为空
        # if 'password' in data and data['password'] is not None:
        #     user.password = data.get('password')

        cloth.name = data.get('name')
        cloth.style = data.get('type')
        cloth.real_sales = data.get('real_sales')
        cloth.isLiked = data.get('isLiked')
        cloth.procity = data.get('procity')
        cloth.applicable_age = data.get('applicable_age')
        cloth.fabric = data.get('fabric')
        cloth.season = data.get('season')
        cloth.price = data.get('price')
        cloth.save()
        return JsonResponse({'message': 'Cloth updated successfully'}, safe=False)

    elif request.method == 'DELETE':
        cloth = ClothList.objects.get(id=clothId)
        cloth.delete()
        return JsonResponse({'message': 'Cloth deleted successfully'})
    elif request.method == 'GET':
        try:
            cloth = ClothList.objects.get(id=clothId)
            cloth_data = {
                "id": cloth.id,
                "name": cloth.item_name,
                "type": cloth.style,
                "img": cloth.pic,
                "real_sales": cloth.real_sales,
                "isLiked": cloth.isLiked,
                "procity": cloth.procity,
                "applicable_age": cloth.applicable_age,
                "fabric": cloth.fabric,
                "season": cloth.season,
                "price": cloth.price
            }
            return JsonResponse(cloth_data)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Cloth not found'}, status=404)


# 服装单价排行前五
def sale_price(request):
    all_data = ClothList.objects.all()

    # 从数据库中获取数据并存储到列表中
    cloth_data = []
    for data in all_data:
        price = data.price
        name = data.item_name
        cloth_data.append({
            "name": name,
            "price": price
        })

    # 对服装数据按照价格进行排序，取前五个并倒序
    sorted_data = sorted(cloth_data, key=lambda x: x["price"], reverse=True)[:5][::-1]

    # 构建柱状图数据
    x_data = [item["name"] for item in sorted_data]
    y_data = [item["price"] for item in sorted_data]

    option = {
        "xAxis": {
            "type": "value",
            "max": 70000,  # 设置最大值为 70000
            "axisLabel": {
                "color": "#fff"
            }
        },

        "yAxis": {
            "type": "category",
            "data": x_data,
            "axisLabel": {
                "color": "#fff"
            }
        },
        "series": [{
            "data": y_data,
            "type": "bar",
            "barWidth": 10,  # 修改柱宽为10
            "barBorderRadius": 30,
            "label": {
                "show": True,
                "position": "right",
                "color": "#fff"
            },
            "itemStyle": {
                "color": "#3fdaff"  # 柱状图颜色
            },
            "tooltip": {
                "trigger": "axis",
                "formatter": "{b}: {c}"
            },

        }],
        "grid": {
            "left": "3%",
            "right": "4%",
            "bottom": "3%",
            "containLabel": True
        },
        "backgroundColor": "#031f2d"
    }

    return JsonResponse(option, safe=False)

def pie1(request):
    if request.method == 'GET':
        cloth_items = MyLove.objects.all()

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

def pie2(request):
    if request.method == 'GET':
        cloth_items = MyLove.objects.all()

        # 使用 defaultdict 初始化一个字典，用于统计每种风格的数量
        style_count = defaultdict(int)

        for item in cloth_items:
            if item.style is not None:
                style_count[item.fabric] += 1

        # 准备饼图所需的数据
        data = []
        for style, count in style_count.items():
            data.append({"name": style, "value": count})

        option = {

            "series": [{
                "name": "Fabric",
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

#矩树图
def age_world(request):
    if request.method == 'GET':
        all_data = ClothList.objects.all()

        # 获取所有适用年龄数据，并排除掉None值
        age_data = [data.applicable_age for data in all_data if data.applicable_age is not None]

        # 统计年龄数据的个数
        age_counts = Counter(age_data)

        # 将年龄数据个数转换为 echarts 需要的数据格式
        data = [{'name': str(age), 'value': count} for age, count in age_counts.items()]

        return JsonResponse({'data': data}, safe=False)


def unify_season(season_str):
    if "春" in season_str:
        return "春"
    elif "夏" in season_str:
        return "夏"
    elif "秋" in season_str:
        return "秋"
    elif "冬" in season_str:
        return "冬"
    else:
        return season_str


def lei_season(request):
    all_data = ClothList.objects.all()

    # 过滤掉'season'字段为None且格式不符合预期的数据
    valid_data = [data for data in all_data if data.season and "年" in data.season]

    season_counts = Counter()
    for item in valid_data:
        # 统一季节词汇
        season = unify_season(item.season)

        # 提取购买人数中的数字部分
        sales = re.findall(r'\d+', item.real_sales)
        if sales:
            # 将提取的数字部分转换为整数并加入对应季节的购买人数总和中
            sales_number = int(sales[0])
            if season in season_counts:
                season_counts[season] += sales_number
            else:
                season_counts[season] = sales_number

    data = {
        'labels': list(season_counts.keys()),
        'values': list(season_counts.values())
    }

    return JsonResponse({'data': data}, safe=False)