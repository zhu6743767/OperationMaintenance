# Generated by Django 4.1.1 on 2023-08-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_alter_envmanager_envmanagername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='envmanager',
            name='EnvManagerName',
            field=models.CharField(default=((1, '生产环境'), (2, '测试环境'), (3, '开发环境')), max_length=16, verbose_name='环境'),
        ),
    ]
