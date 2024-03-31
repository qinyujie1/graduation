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
    path("usermanage/", views.user_manage),  # 用户管理
    path("usermanage/<int:userId>/", views.user_manage1),  # 用户管理

]
