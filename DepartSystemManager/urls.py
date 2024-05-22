"""DepartSystemManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app01 import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # 首页
    path('index/', views.index, name='index'),
    path('index/add/', views.index_add, name='index/add/'),


    # 机构管理
    path('depart/', views.depart, name='depart/'),
    path('depart/add/', views.depart_add, name='depart/add/'),
    path('depart/delete/', views.depart_delete),
    path('depart/<int:nid>/edit', views.depart_edit),


    # IP地址管理
    path('ip_manager/', views.ip_manager, name='ip_manager'),
    path('ip_manager/ip_add/', views.ip_add, name='ip_manager/ip_add/'),

    # 业务系统管理
    path('system/', views.system, name='system'),
    path('system/add/', views.system_add, name='system/add/'),

    # 端口管理
    path('server/port/', views.server_port, name='server/port/'),
    path('server/port/add/', views.server_port_add, name='server/port/add'),
]
