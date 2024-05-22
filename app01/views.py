# coding:utf-8

from django.shortcuts import render, redirect
from app01 import forms
from app01 import models


# 首页
def index(request):
    queryset = models.DepartSystemName.objects.all()

    return render(request, 'index.html', {'queryset': queryset})


# 添加映射
def index_add(request):
    if request.method == "GET":
        form = forms.DepartSystemNameModelForm()
        return render(request, 'departsystem_add.html', {'form': form})

    # 用户通过POST方式提交数据，并进行数据校验
    form = forms.DepartSystemNameModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存数据到数据库
        form.save()
        return redirect('/index')

    # 如果数据校验失败，在页面上显示错误信息
    return render(request, 'departsystem_add.html', {'form': form})

#############################################################################################################
# 机构列表
def depart(request):
    queryset = models.Department.objects.all()

    return render(request, 'depart.html', {'queryset': queryset})


# 添加机构
def depart_add(request):
    if request.method == "GET":
        form = forms.DepartModelForm()
        return render(request, 'depart_add.html', {'form': form})

    # 用户通过POST方式提交数据，并进行数据校验
    form = forms.DepartModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存数据到数据库
        form.save()
        return redirect('/depart')

    # 如果数据校验失败，在页面上显示错误信息
    return render(request, 'depart_add.html', {'form': form})


# 编辑机构
def depart_edit(request, nid):
    """编辑部门"""
    if request.method == "GET":
        # 根据ID获取对应的数据
        row_object = models.Department.objects.filter(id=nid).first()
        # 跳转部门列表
        return render(request, 'depart_edit.html', {"row_object": row_object})

    # 获取用户提交的数据
    title = request.POST.get('title')
    text = request.POST.get('text')

    # 根据ID找到数据库中的数据并进行数据更新
    models.Department.objects.filter(id=nid).update(title=title, text=text)

    # 跳转部门列表
    return redirect("/depart/")


# 删除部门
def depart_delete(request):
    """删除部门"""
    # 获取ID
    nid = request.GET.get('nid')
    # 删除ID对应的数据
    models.Department.objects.filter(id=nid).delete()
    # 跳转部门列表
    return redirect("/depart/")


#############################################################################################################
# IP地址
def ip_manager(request):
    queryset = models.IpManager.objects.all()
    return render(request, 'ip_manager.html', {'queryset': queryset})


# 添加IP地址
def ip_add(request):
    if request.method == "GET":
        form = forms.IpModelForm()
        return render(request, 'ip_add.html', {'form': form})

    # 用户通过POST方式提交数据，并进行数据校验
    form = forms.IpModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存数据到数据库
        form.save()
        return redirect('/ip_manager/')

    # 如果数据校验失败，在页面上显示错误信息
    return render(request, 'ip_add.html', {'form': form})


#############################################################################################################
# 业务系统
def system(request):
    queryset = models.BusinessServer.objects.all()
    print(queryset)
    for obj in queryset:
        print(obj.id)
    return render(request, 'system.html', {'queryset': queryset})


# 业务系统添加
"""
def system_add(request):
    if request.method == "GET":
        form = forms.BusinessServerNameModelForm()
        return render(request, 'system_add.html', {'form': form})

    # 用户通过POST方式提交数据，并进行数据校验
    form = forms.BusinessServerNameModelForm(data=request.POST)
    print(form)
    if form.is_valid():
        # 如果数据合法，保存数据到数据库
        form.save()
        return redirect('/system/')

    # 如果数据校验失败，在页面上显示错误信息
    return render(request, 'system_add.html', {'form': form})
"""
def system_add(request):
    if request.method == "GET":
        form = forms.BusinessServerNameModelForm()
        return render(request, 'system_add.html', {'form': form})

    # 用户通过POST方式提交数据，并进行数据校验
    form = forms.BusinessServerNameModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存数据到数据库
        form.save()
        return redirect('/system/')

    # 如果数据校验失败，在页面上显示错误信息
    return render(request, 'system_add.html', {'form': form})

#############################################################################################################
# 服务端口
def server_port(request):
    queryset = models.ServerPort.objects.all()

    return render(request, 'server_port.html', {'queryset': queryset})


# 端口添加
def server_port_add(request):
    if request.method == "GET":
        form = forms.ServerPortModelForm()
        return render(request, 'server_port_add.html', {'form': form})

    # 用户通过POST方式提交数据，并进行数据校验
    form = forms.ServerPortModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存数据到数据库
        form.save()
        return redirect('/server/port/')

    # 如果数据校验失败，在页面上显示错误信息
    return render(request, 'server_port_add.html', {'form': form})
