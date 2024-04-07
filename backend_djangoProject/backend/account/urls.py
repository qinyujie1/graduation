from ..account import views
from django.urls import path, re_path, include

urlpatterns = [
    path("login/", views.login),  # 登录
    path("logout/", views.logout1),  # 退出登录
    path("register/", views.register),  # 注册
    path("index/", views.index),  # 首页
    path("list/", views.list1),  # 服装列表
    path("detail/<int:nid>/", views.detail),  # 服装列表
    path("mylove/", views.mylove),  # 我的喜欢
    path("recommend/", views.recommend),  # 协同过滤
    path("dashboards/", views.dashboards),  # 总览柱状图
    path("dashboards1/", views.dashboards1),  # 总览饼图
    path("dashboards2/", views.admin_login_dashbords),  # admin销售地销售人数
    path("dashboards3/", views.admin_login_dashbords1),  # admin销售总额
    path("dashboards4/", views.admin_login_dashbords2),  # admin销售总人数
    path("dashboards5/", views.admin_login_dashbords3),  # admin服装总数量
    path("dashboards6/", views.sale_price),  # 服装单价排行
    path("dashboards7/", views.pie1),  # 我的喜欢服装类型
    path("dashboards8/", views.pie2),  # 我的喜欢服装面料
    path("dashboards9/", views.age_world),  # 适合年龄 矩树图
    path("dashboards10/", views.lei_season),  # 适合季节 雷达图
    path("usermanage/", views.user_manage),  # 用户管理 查看新增
    path("usermanage/<int:userId>/", views.user_manage1),  # 用户管理 修改删除
    path("inventory_management/", views.inventory_management),  # 库存管理 查看新增
    path("inventory_management/<int:clothId>/", views.inventory_management1),  # 库存管理 修改删除

]
