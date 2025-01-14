#_*_encoding utf-8 *_*
from django import forms
from django.forms import ModelForm
from mainsite import models
from captcha.fields import CaptchaField		

class  ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = models.Contact
        fields = ['u_name','u_birthday','u_school','u_email','u_suggest','u_message']
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['u_name'].label = '暱稱'
        self.fields['u_birthday'].label = '生日'
        self.fields['u_school'].label = '是否在學'
        self.fields['u_email'].label = '電子郵件'
        self.fields['u_suggest'].label = '建議分類'
        self.fields['u_message'].label = '留言建議' 
        self.fields['captcha'].label = '確定不是機器人'  
