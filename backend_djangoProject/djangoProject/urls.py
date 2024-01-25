from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('api/', include('backend.account.urls'))
]
