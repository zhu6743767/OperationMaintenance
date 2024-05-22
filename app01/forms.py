# coding:utf-8

from django import forms
from app01 import models


# 定义depart 的ModelForm的类
class DepartModelForm(forms.ModelForm):
    class Meta:
        model = models.Department
        fields = ['DepartName', 'DepartCode', 'DepartInfo', 'DepartAddress', 'DepartIp']

    # 给所有字段在html显示中，加入样式！
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加class="form-contorl"样式
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


# 定义IpManager 的ModelForm的类
class IpModelForm(forms.ModelForm):
    class Meta:
        model = models.IpManager
        fields = ['IpField', 'IpType', 'IpEnv',]

    # 给所有字段在html显示中，加入样式！
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加class="form-contorl"样式
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


# 定义SystemName 的ModelForm的类
class BusinessServerNameModelForm(forms.ModelForm):
    class Meta:
        model = models.BusinessServer
        fields = ['BusinessName', 'BusinessServerPort', 'BusinessServerEnv']
        print(fields)
    # 给所有字段在html显示中，加入样式！
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加class="form-contorl"样式
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


# 定义ServerPort 的ModelForm的类
class ServerPortModelForm(forms.ModelForm):
    class Meta:
        model = models.ServerPort
        fields = ['PortName', 'PortNum', 'PortType']

    # 给所有字段在html显示中，加入样式！
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加class="form-contorl"样式
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


# 定义DepartSystemName 的ModelForm类
class DepartSystemNameModelForm(forms.ModelForm):
    class Meta:
        model = models.DepartSystemName
        fields = ['Department', 'IpManager', 'ServerPort', 'SystemName']

    # 给所有字段在html显示中，加入样式！
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加class="form-contorl"样式
        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}

