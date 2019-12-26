#传递token的接口方法
import json
import unittest
from common.configHttp import RunMain
from common.GetToken import gettoken
import paramunittest
import geturlParams
import urllib.parse
import readExcel
url = geturlParams.geturlParams().get_Url()# 调用我们的geturlParams获取我们拼接的URL
print(url)
login_xls = readExcel.readExcel().get_xls('userCase.xlsx', 'login')
print(login_xls)
@paramunittest.parametrized(*login_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, case_name, path, query, method):
        """
        set params
        :param case_name:
        :param path
        :param query
        :param method
        :return:
        """
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = query
        self.method = str(method)

    def description(self):
        """
        test report description
        :return:
        """
        self.case_name

    def setUp(self):
        """
        :return:
        """
        print(self.case_name+"测试开始前准备")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):# 断言
        """
        check test result
        :return:
        """
        new_url = url + self.path
        print(new_url)
        data1 = eval(self.query) #字符串转换成字典
        header = gettoken()
        info = RunMain().run_main(self.method, new_url, data1, header)# 根据Excel中的method调用run_main来进行requests请求，并拿到响应
        print(info)
        if self.case_name == 'login':# 如果case_name是login，说明合法，返回的code应该为200
            self.assertEqual(info['code'], 200)



