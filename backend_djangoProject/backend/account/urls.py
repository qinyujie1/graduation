from ..account import views
from django.urls import path, re_path, include

urlpatterns = [
    path("login/", views.login), #登录
    path("logout/", views.logout), #退出登录
    path("register/", views.register), #注册
    path("index/",views.index), #首页
    path("list/",views.list),#服装列表
    path("mylove/",views.mylove),#我的喜欢
    path("recommend/",views.recommend),#协同过滤
    path("dashboards/",views.dashboards),#总览柱状图
    path("dashboards1/",views.dashboards1)#总览饼图

]
