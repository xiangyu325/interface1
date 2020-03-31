import requests
from common.Log import logger
from common.GetToken import gettoken
logger = logger
class RunMain():
    def send_post(self, url, data, header):  # 定义一个方法，传入需要的参数url和data
        # 参数必须按照url、data顺序传入
        result = requests.post(url=url, json=data, headers=header).json() # 因为这里要封装post方法，所以这里的url和data值不能写死
        return result

    def send_get(self, url, data, header):
        result = requests.get(url=url, params=data, headers=header).json()
        return result

    def run_main(self, method, url=None, data=None, header=None):  # 定义一个run_main函数，通过传过来的method来进行不同的get或post请求
        result = None
        if method == 'post':
            result = self.send_post(url, data, header)
        elif method == 'get':
            result = self.send_get(url, data,header)
        else:
            print("method值错误！！！")
        return result

if __name__ == '__main__':  # 通过写死参数，来验证我们写的请求是否正确
    a = {"password": "Scaijia123", "platform": 1,   "tenant_domain": "web",  "username": "S19bk_t_admin"}
    result1 = RunMain().run_main('post', 'https://t-u1.sancaijia.net/api/v1/user/backyard_login',a,None)
    result2 = RunMain().run_main('get', 'https://t-u1.sancaijia.net/api/v1/user/address/address_list',None,gettoken())
    print(result1)
    print(result2)
