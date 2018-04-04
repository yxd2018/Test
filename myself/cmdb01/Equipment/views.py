#coding:utf-8
from django.http import JsonResponse,HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from models import Equipment
import paramiko
import os
import time,hmac,hashlib,json
from User import forms

# Create your views here.
def vueTest(request):
    return render(request, 'vueTest.html', locals())

def eqList(request):
    register = forms.Register()
    return render(request, "eqlist.html", locals())

#获取连接
def getConnection(ipaddress,username,password, fun):
    """
    :param ipaddress:
    :param username:
    :param password:
    连接服务器，生成实例
    :return:
    """
    result = {"state": "error", "data": ""}
    try:
        transport = paramiko.Transport((ipaddress, 22))
        transport.connect(username=username, password=password)
    except Exception as e:
        result["data"] = str(e)
    else:
        fun(transport, ipaddress, username, password)
        result["state"] = "success"
        result["data"] = transport
    return result

#文件上传
def putFile(transport, ipaddress, usernmae, password):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR,"Equipment/CMDBClient")
    sftp = paramiko.SFTPClient.from_transport(transport)

    try:
        sftp.put(os.path.join(file_path,"main.py"), "/opt/CMDB/main.py")
        sftp.put(os.path.join(file_path,"getData.py"), "/opt/CMDB/getData.py")
        sftp.put(os.path.join(file_path,"sendData.py"), "/opt/CMDB/sendData.py")
    except Exception as e:
        print e
    finally:
        transport.close()

def doCommand(transport, ipaddress, username, password):
    createCommand = "mkdir /opt/CMDB"
    testCommand = "ls /opt"
    execCommand = "python /opt/CMDB/main.py"
    #进行ssh连接
    ssh = paramiko.SSHClient()
    ssh._transport = transport
    #创建目录
    try:
        ssh.exec_command(createCommand)
        while True:
            stdin,stdout,stderr = ssh.exec_command(testCommand)
            if "CMDB" in stdout.read():
                getConnection(ipaddress, username, password, putFile)
                ssh.exec_command(execCommand)
                break
    except Exception as e:
        print e
    finally:
        transport.close()

#添加设备
def addEquipment(request):
    result = {"state": "error", "data": ""}
    if request.method == "POST":
        requestData = request.POST
        ipaddress = requestData.get("ipaddress", "")
        username = requestData.get("username", "")
        password = requestData.get("password", "")
        if ipaddress and username and password:
            #调用方法执行上传
            getConnection(ipaddress, username, password, doCommand)
            result["state"] = "success"
            result["data"] = "success"
        else:
            result["data"] = "ip and username and password not be null"
    else:
        result["data"] = "you request must be post"
    return JsonResponse(result)
def eqDatas(request,pagenum):

    pagenum = int(pagenum)
    start = (pagenum-1)*10
    end = pagenum*10
    eq_len = 10

    all_data = Equipment.objects.all()[start:end]
    result_list = []
    for data in all_data:
        dicts = {
            "disk":data.disk,
            "sys_version":data.sys_version,
            "mac":data.mac,
            "memory":data.memory,
            "cpu_count":data.cpu_count,
            "ip":data.ip,
            "hostname":data.hostname,
            "sys_type":data.sys_type,
            "id":data.id
        }
        result_list.append(dicts)
    a,b = divmod(eq_len, 10)
    if b!=0:
        Prange = range(1, a+2)
    else:
        Prange = range(1, a+1)
    Prange.reverse()
    result = {"result": result_list, "Prange": Prange}
    return JsonResponse(result)

#接口保存部分
@csrf_exempt
def equip_api(request):
    result = {"statue": "error", "data": ""}
    if request.method == "POST":
        requestData = request.POST
        hostname = requestData.get("hostname")
        mac = requestData.get("mac")
        ip = request.META["REMOTE_ADDR"]
        disk = requestData.get("disk")
        sys_type = requestData.get("systerm")
        sys_version = requestData.get("sys_version")
        memory = requestData.get("memory")
        cpu_count = requestData.get("cpu_count")
        try:
            eq = Equipment()
            eq.hostname = hostname
            eq.mac = mac
            eq.ip = ip
            eq.disk = disk
            eq.memory = memory
            eq.cpu_count = cpu_count
            eq.sys_type = sys_type
            eq.sys_version = sys_version
            eq.save()
        except Exception as e:
            result["data"] = str(e)
        else:
            result["statue"] = "success"
            result["data"] = "you data is saved"
    else:
        result["data"] = "request must be post"
    return JsonResponse(result)

def gateone(request):
    return render(request, "gateone.html", locals())

def Terminal(request,id):
    id = int(id)
    equipment = Equipment.objects.get(id=id)
    ip = equipment.ip
    port=22
    username = "root"
    return render(request, "Terminal.html", locals())

def create_signature(secret,*parts):
    hash = hmac.new(secret,digestmod=hashlib.sha1)
    for parts in parts:
        hash.update(str(parts))
    return hash.hexdigest()
def get_auth_obj(request):
    user = request.user.username
    gateone_server = "https://192.168.1.104:443"
    secret = "ZjRjYTQxYThkOTNjNGI4NDkyYWE5ZWJiOThmMTE4N2MxY"
    api_key = "YTA2NDA3NTU3ZDZjNDY4YWE4YjYyMTE0YjkzNDZlMDMyY"

    authobj = {
        'api_key': api_key,
        'upn': "gateone",
        'timestamp': str(int(time.time() * 1000)),
        'signature_method': 'HMAC-SHA1',
        'api_version': '1.0'
    }
    my_hash = hmac.new(secret, digestmod=hashlib.sha1)
    my_hash.update(authobj['api_key'] + authobj['upn'] + authobj['timestamp'])

    authobj['signature'] = my_hash.hexdigest()
    auth_info_and_server = {"url": gateone_server, "auth": authobj}
    valid_json_auth_info = json.dumps(auth_info_and_server)
    return HttpResponse(valid_json_auth_info)

def morris(request):
    return render(request, "morris.html", locals())
