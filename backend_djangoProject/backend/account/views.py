import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

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


# def recommend(request):
#     if request.method == 'POST':
#         user_clothes = MyLove.objects.filter(isLiked=True)
#         all_clothes = ClothList.objects.all()
#
#         # 提取用户喜欢的服装描述信息
#         user_descriptions = [
#             f"{cloth.style} {cloth.price} {cloth.real_sales} {cloth.procity} {cloth.applicable_age} {cloth.fabric} {cloth.season}"
#             for cloth in user_clothes if all([cloth.style, cloth.price, cloth.real_sales, cloth.procity, cloth.applicable_age, cloth.fabric, cloth.season])
#         ]
#
#         # 使用TF-IDF向量化用户喜欢的服装描述信息
#         tfidf = TfidfVectorizer(stop_words='english')
#         tfidf_matrix = tfidf.fit_transform(user_descriptions)
#
#         # 计算所有服装之间的相似度矩阵
#         all_descriptions = [
#             f"{cloth.style} {cloth.price} {cloth.real_sales} {cloth.procity} {cloth.applicable_age} {cloth.fabric} {cloth.season}"
#             for cloth in all_clothes if all([cloth.style, cloth.price, cloth.real_sales, cloth.procity, cloth.applicable_age, cloth.fabric, cloth.season])
#         ]
#         all_tfidf_matrix = tfidf.transform(all_descriptions)
#         cosine_sim_all = cosine_similarity(all_tfidf_matrix, tfidf_matrix)
#
#         recommended_clothes = []
#         for idx, user_cloth in enumerate(user_clothes):
#             similar_indices = cosine_sim_all[:, idx].argsort()[::-1]  # 按相似度排序
#             for i in similar_indices:
#                 try:
#                     recommended_clothes.append(all_clothes.get(pk=i))
#                 except ClothList.DoesNotExist:
#                     pass
#
#         # 去除重复推荐的服装
#         unique_recommended_clothes = recommended_clothes
#
#         # 将推荐的服装转换为字典格式
#         formatted_recommended_clothes = []
#         for cloth in unique_recommended_clothes:
#             formatted_cloth = {
#                 "item_name": cloth.item_name,
#                 "style": cloth.style,
#                 "price": cloth.price,
#                 "real_sales": cloth.real_sales,
#                 "pic": cloth.pic,
#                 "procity": cloth.procity,
#                 "applicable_age": cloth.applicable_age,
#                 "fabric": cloth.fabric,
#                 "season": cloth.season,
#                 # 添加其他属性，根据需要继续添加
#             }
#             formatted_recommended_clothes.append(formatted_cloth)
#
#         # 添加总推荐服装数量
#         total_recommendations = len(formatted_recommended_clothes)
#         response_data = {
#             "total_recommendations": total_recommendations,
#             "recommended_clothes": formatted_recommended_clothes
#         }
#         print(2222222)
#         print(11111111+response_data)
#         return JsonResponse(response_data, safe=False)
def recommend(request):
    if request.method == 'POST':
        user_clothes = MyLove.objects.filter(isLiked=True)
        all_clothes = ClothList.objects.all()

        # 提取用户喜欢的服装特征
        user_features = []
        for cloth in user_clothes:
            features = [cloth.style, cloth.price, cloth.real_sales, cloth.procity, cloth.applicable_age, cloth.fabric, cloth.season]
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
            features = [cloth.style, cloth.price, cloth.real_sales, cloth.procity, cloth.applicable_age, cloth.fabric, cloth.season]
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



