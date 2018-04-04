#coding:utf-8
import re
from django import forms
from django.forms import ValidationError
from models import CmdbUser
from cmdb01 import views

#建立表单
class Register(forms.Form):
    username = forms.CharField(
        max_length=32,
        min_length=6,
        label='用户名',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'用户名'})
    )
    password = forms.CharField(
        max_length=32,
        min_length=6,
        label='密码',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '密码'})
    )
    email = forms.CharField(
        max_length=32,
        min_length=6,
        label="邮箱",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '邮箱'})
    )
    phone = forms.CharField(
        max_length=32,
        min_length=11,
        label='电话',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '电话'})
    )
    photo = forms.ImageField(label='用户头像', )

    #校验
    def clean_username(self):
        username = self.cleaned_data.get('username') #获取提交的电话值
        result = views.valid_username(username)
        if result == username:
            return username
        else:
            raise ValidationError(result)  #否则就是重复

    def clean_phone(self):
        phone = self.cleaned_data.get('phone') #获取提交的电话值
        result = views.valid_phone(phone)
        if result == phone:
            return phone
        else:
            raise ValidationError(result)

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if password.isdigit():
            raise ValidationError('密码不可以完全以数字组成')
        elif password.isalnum():
            raise ValidationError('密码不可以完全以数字或者字母组成')
        else:
            return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        res = re.match(r'\w+@\w+\.[a-zA-Z]+',email)
        if res:
            return email
        else:
            raise ValidationError('邮箱格式错误')