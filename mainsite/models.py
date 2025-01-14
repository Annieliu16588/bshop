#_*_encoding: utf-8 _*_
from django.db import models

# Create your models here.

#客服寄信
class  Contact(models.Model):
    """docstring for  ContactForm"""
    SUGGEST=[
       ['EXTERIOR','網站外觀'],
       ['USABILITY','可用性'],
       ['CONTNET','內容建議'],
       ['USER_P','帳號問題'],
       ['AUTHORITY','權限請求'],
       ['OTHERS','其它建議']
    ]
    u_name = models.CharField(default='不知道要取什麼',max_length=20,verbose_name ='暱稱')
    u_birthday = models.DateField(null=True, blank=False,verbose_name ='建議者生日')
    u_school = models.BooleanField(default=False,verbose_name ='是否在學')
    u_suggest = models.CharField(default=False,max_length=10, choices=SUGGEST,verbose_name='建議分類')
    u_email = models.CharField(max_length=25,verbose_name ='聯絡方式（電子郵件）')
    u_message = models.TextField(null=False,verbose_name ='建議')
    def __str__(self):
        return self.u_suggest
#產品資訊
class Publishing (models.Model):
    name = models.CharField(max_length=10,verbose_name ='出版商')
    def __str__(self):
        return self.name

class Product(models.Model):
    publishing = models.ForeignKey(Publishing , on_delete=models.SET_DEFAULT ,default='3')
    name= models.CharField(default='書名', max_length=20, verbose_name ='書籍名稱',null=True)
    author = models.CharField(max_length=15, default='作者姓名',verbose_name='書籍作者')
    description = models.TextField(default='暫時無說明',verbose_name ='書籍簡介')
    year = models.PositiveIntegerField(default=2016,verbose_name ='出版年')
    price = models.PositiveIntegerField(default=0,verbose_name ='價格')

    # def __str__(self):
    #     return self.name

class PPhoto(models.Model):
    error = '該書籍已絕版'
    product = models.ForeignKey(Product, on_delete=models.SET_DEFAULT ,default='3')
    description = models.CharField(max_length=20, default='書籍狀況')
    url = models.URLField(default='https://i.ibb.co/5vmRTyz/d350c383c6311ba3-thumb-600.jpg')

    def __str__(self):
        return self.description



