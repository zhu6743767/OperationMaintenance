from django.db import models
from enum import Enum, EnumMeta

# Create your models here.

EnvManager_choices = (
    ("生产环境", "生产环境"), 
    ("测试环境", "测试环境"), 
    ("开发环境", "开发环境"),
   )

# 环境
class EnvManager(Enum):
    produce =  "生产环境"
    testing = "测试环境"
    develop = "开发环境"

# IP地址
class IpManager(models.Model):
    IpTypes_choices = ((1, "业务地址"), (2, "映射地址"), (3, "服务器地址"),)
    IpField = models.GenericIPAddressField(protocol="IPv4", verbose_name="IP地址")
    IpType = models.SmallIntegerField(verbose_name="类别", choices=IpTypes_choices)
    IpEnv = models.CharField(max_length=16, choices=EnvManager_choices,default=EnvManager.produce)

    def __str__(self):
        return self.IpField

    class Meta:
        db_table = 'IpField'
        verbose_name = 'IP地址 '
        verbose_name_plural = verbose_name


# 机构
class Department(models.Model):
    DepartName = models.CharField(verbose_name='机构名称', max_length=64)
    DepartCode = models.CharField(verbose_name='机构社会信用代码', max_length=18)
    DepartInfo = models.TextField(verbose_name='机构简介', max_length=255)
    DepartAddress = models.TextField(verbose_name='机构地址', max_length=255)
    DepartIp = models.OneToOneField(IpManager, verbose_name='业务IP地址', on_delete=models.CASCADE)

    def __str__(self):
        return self.DepartName

    class Meta:
        db_table = 'DepartName'
        verbose_name = '机构名称 '
        verbose_name_plural = verbose_name


# 端口
class ServerPort(models.Model):
    """服务端口"""
    TypePort_choices = ((1, "TCP"), (2, "UDP"),)
    TypeName_choices = ((1, "映射端口"), (2, "服务端口"),)
    PortName = models.SmallIntegerField(verbose_name="端口服务", choices=TypeName_choices)
    PortNum = models.IntegerField(verbose_name="端口号")
    PortType = models.SmallIntegerField(verbose_name="端口协议", choices=TypePort_choices)

    def __str__(self):
        return str(self.PortNum)

    class Meta:
        db_table = 'PortNum'
        verbose_name = '端口号 '
        verbose_name_plural = verbose_name


# 业务系统名称
class BusinessServer(models.Model):
    """业务系统名称"""
    BusinessName = models.CharField(verbose_name='业务系统名称', max_length=64)
    BusinessServerPort = models.OneToOneField(ServerPort, verbose_name='服务端口', on_delete=models.CASCADE)
    BusinessServerEnv = models.CharField(max_length=16, verbose_name="业务系统环境",choices=EnvManager_choices,default=EnvManager.produce)
    def __str__(self):
        return self.BusinessName

    class Meta:
        db_table = 'BusinessServer'
        verbose_name = '业务系统名称 '
        verbose_name_plural = verbose_name


# 机构业务系统映射
class DepartSystemName(models.Model):
    Department = models.ForeignKey(Department,verbose_name='机构信息', on_delete=models.CASCADE)
    IpManager = models.ForeignKey(IpManager,   on_delete=models.CASCADE)
    ServerPort = models.ForeignKey(ServerPort,  on_delete=models.CASCADE)
    SystemName = models.ForeignKey(BusinessServer, on_delete=models.CASCADE)


    def __str__(self):
        return self.Department_Name

    class Meta:
        db_table = 'Department_Name'
        verbose_name = '机构业务系统名称 '
        verbose_name_plural = verbose_name
