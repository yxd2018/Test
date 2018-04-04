#coding:utf-8
import os
import uuid
import psutil
"""
hostname
ip
mac
systerm
sys_version
cpu_count
memory
disk
"""
class Getdata:
    def __init__(self):
        self.result = {}
        self.sys = os.name
        if self.sys == 'nt':
            self.systerm = 'Windows'
            self.hostname = os.getenv('computername')
        elif self.sys == 'posix':
            self.systerm = 'Linux'
            self.hostname = os.popen("hostname").read()
        else:
            self.systerm = 'Unix'
            self.hostname = "unknown"
    def get_hostname(self):
        return self.hostname
    def get_systerm(self):
        return self.systerm
    def get_mac(self):
        mac = uuid.UUID(int = uuid.getnode()).hex[-12:]
        result = ":".join([mac[e:e+2] for e in range(0,11,2)])
        return result
    def get_sys_version(self):
        version = os.popen("cat /etc/issue").read()
        return version
    def get_cpu_count(self):
        count = psutil.cpu_count()
        return str(count)
    def get_memory(self):
        memory = str(psutil.virtual_memory().total)
        return str(memory)
    def get_disk(self):
        disk = str(psutil.disk_usage('/').total)
        return str(disk)
    def getData(self):
        data_method = Getdata.__dict__
        for key,value in data_method.items():
            if "get_"in key and callable(value):
                name = key.replace("get_","")
                self.result[name] = str(value(self)).replace("\n","").replace("\r","").replace("\\","")
        return self.result


if __name__=="__main__":
    data = Getdata()
    data.getData()
    result = data.getData()
    print result