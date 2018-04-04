#coding:utf-8
from django.shortcuts import render
from cmdb01.views import valid_phone,getmd5,valid_username,loginvalid
from django.http import JsonResponse,HttpResponseRedirect
from forms import Register  #导入表单
from models import CmdbUser  #导入数据库
from PIL import Image

def login(request):

    if request.method == "POST":
        #如果是post请求根据name进行数据获取
        phone = request.POST["phone"]
        password = request.POST["password"]
        #尝试获取数据库里的手机号信息
        try:
            user = CmdbUser.objects.get(phone=phone)
        #如果获取失败,返回登录页
        except:
            return HttpResponseRedirect('login')
        else:
            md5_password = getmd5(password)
            if user.password == md5_password:
                response = HttpResponseRedirect('index')#实例化响应
                response.set_cookie("username",user.username)
                request.session['username'] = user.username
                request.session['isLogin'] = True
                token = request.COOKIES.get("token")
                if token:
                    return response
                else:
                    return HttpResponseRedirect('login')
            else:
                return HttpResponseRedirect('login')
    response = render(request, 'login.html')
    response.set_cookie("token", "hello world")
    return response

@loginvalid
def index(request):
    register = Register()
    return render(request, 'index.html', locals())

def base(request):
    register = Register()
    return render(request, 'base.html', locals())

#接受ajax函数的初步描写
def register(request):
    res = {"type": "error", "data": ""}
    if request.method == "POST":
        #获取值
        reg = Register(request.POST, request.FILES)  #对数据进行校验
        #外部数据方式
        # reg = Register({'username':'while','password':'while123!'})

        if reg.is_valid():
            cleaned_data = reg.cleaned_data  #验证通过典形式的数据
            username = cleaned_data['username']
            password = cleaned_data['password']
            email = cleaned_data['email']
            phone = cleaned_data['phone']
            photo = cleaned_data['photo']

            user = CmdbUser()
            user.username = username
            user.password = getmd5(password) #加密密码
            user.email = email
            user.phone = phone
            user.photo = photo

            name = 'static/image/'+photo.name
            img = Image.open(photo) #先打开图片源码
            img.save(name)  #保存图片
            #数据库当中存储图片的路径
            user.photo = 'image/'+photo.name

            user.save() #保存数据库

            res["type"] = "success"
            res["data"] = "success"
        else:
            res["data"] = reg.errors
    else:
        res["data"] = "request error"
    return JsonResponse(res)

#手机号校验
def phone_valid(request):
    res = {"type": "error", "data": ""}
    if request.method == "GET":
        phone = request.GET["phone"]
        result = valid_phone(phone)
        if phone == result:
            res["type"] = "success"
        else:
            res["data"] = result
    else:
        res["data"] = "request must be GET"
    return JsonResponse(res)

#用户名校验
def username_valid(request):
    res = {"type": "error", "data": ""}
    if request.method =="GET":
        username = request.GET["username"]
        result = valid_username(username)
        if username == result:
            res["type"] = "success"
        else:
            res["data"] = result
    else:
        res["data"] = "request must be GET"
    return JsonResponse(res)

