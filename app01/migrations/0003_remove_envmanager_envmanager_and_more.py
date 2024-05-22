# Generated by Django 4.1.1 on 2023-08-30 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_alter_envmanager_envmanager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='envmanager',
            name='EnvManager',
        ),
        migrations.AddField(
            model_name='envmanager',
            name='EnvManagerName',
            field=models.SmallIntegerField(choices=[(1, '生产环境'), (2, '测试环境'), (3, '开发环境')], default=1, verbose_name='环境'),
            preserve_default=False,
        ),
    ]