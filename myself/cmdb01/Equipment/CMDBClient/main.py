#coding:utf-8
from getData import Getdata
from sendData import Sender
import datetime

try:
    #url接口地址
    url = "http://192.168.1.103:8000/eq/equip_api"

    #采集到的数据
    data = Getdata()
    sendData = data.getData()

    #开始请求发送
    sender = Sender(url, sendData)
    sender.get_request()
    response = sender.get_response()
    #返回响应
    print response
except Exception as e:
    with open("/opt/CMDB/log.txt", "wb") as f:
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = "[%s]:%s\n"%(time, str(e))
        f.write(content)


#
# #url接口地址
# url = "http://192.168.1.102:8000/eq/equip_api"
#
# #采集到的数据
# data = Getdata()
# sendData = data.getData()
#
# #开始请求发送
# sender = Sender(url, sendData)
# sender.get_request()
# response = sender.get_response()
# #返回响应
# print response