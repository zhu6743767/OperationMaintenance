# Generated by Django 4.1.1 on 2023-08-31 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_alter_businessserver_businessserverport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessserver',
            name='BusinessServerPort',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.serverport', verbose_name='服务端口'),
        ),
    ]
