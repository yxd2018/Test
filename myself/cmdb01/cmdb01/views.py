#coding:utf-8
from django.shortcuts import render
from User.models import CmdbUser
import hashlib
from django.http import HttpResponseRedirect

#校验电话重复
def valid_phone(phone):
    #尝试从数据库中获取该号码
    try:
        user = CmdbUser.objects.get(phone=phone)
    #假如不存在，返回phone
    except:
        return phone
    else:
        return '手机号重复'

#校验用户名重复
def valid_username(username):
    try:
        user = CmdbUser.objects.get(username=username)
    except:
        return username  # 假如不存在，返回username
    else:
        return '用户名重复'
#加密函数
def getmd5(password):
    md5 = hashlib.md5()
    md5.update(password)
    return md5.hexdigest()


#cookie校验装饰器
def loginvalid(fun):
    def inner(request, *args, **kwargs):
        cookie = request.COOKIES
        c_username = cookie.get('username')
        s_username = request.session.get('username')
        islogin = request.session.get('isLogin')
        if c_username and s_username and c_username == s_username and islogin :
            return fun(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('login')
    return inner

