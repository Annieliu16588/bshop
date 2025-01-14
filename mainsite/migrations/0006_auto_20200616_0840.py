# Generated by Django 3.0.6 on 2020-06-16 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_auto_20200616_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='u_name',
            field=models.CharField(default='想不到', max_length=20, verbose_name='暱稱'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='u_birthday',
            field=models.DateField(null=True, verbose_name='建議者生日'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='u_email',
            field=models.CharField(max_length=25, verbose_name='建議者電子郵件'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='u_message',
            field=models.TextField(verbose_name='建議'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='u_school',
            field=models.BooleanField(default=False, verbose_name='是否在學'),
        ),
    ]
