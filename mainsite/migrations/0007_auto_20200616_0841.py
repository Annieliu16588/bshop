# Generated by Django 3.0.6 on 2020-06-16 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_auto_20200616_0840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='u_name',
            field=models.CharField(default='不知道要取什麼名字', max_length=20, verbose_name='暱稱'),
        ),
    ]
