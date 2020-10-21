# conding = utf-8
import requests
import time
import os
import pytest
import unittest
from Jzt_api.api_Jzt import Jzt_Api
from HTMLTestRunner import HTMLTestRunner


class Testcases(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.jzt_api = Jzt_Api()
        print("金智塔开始进行测试！")

    @classmethod
    def tearDownClass(cls) -> None:
        print("金智塔接口测试结束！")

    def test01(self):  # 账号密码正确
        test01 = self.jzt_api.login('15123901004', '123456')
        self.assertEqual(test01['status'], 200, '测试失败')

    def test02(self):  # 账号错误
        test02 = self.jzt_api.login('151239010041', '123456')
        self.assertEqual(test02['status'], 200, '测试失败')

    def test03(self):  # 密码错误
        test03 = self.jzt_api.login('15123901004', '1234567')
        self.assertEqual(test03['status'], 200, '测试失败')

    def test04(self):  # 查询ID为2020的用户
        ss = self.jzt_api.login('15123901004', '123456')
        token = self.jzt_api.get_token(ss, 'token_name')
        test04 = self.jzt_api.my_home('2020', token)
        self.assertEqual(test04['status'], 200, '测试失败')

    def test05(self):  # 查询ID为2030的用户
        ss = self.jzt_api.login('15123901004', '123456')
        token = self.jzt_api.get_token(ss, 'token_name')
        test05 = self.jzt_api.my_home('2030', token)
        self.assertEqual(test05['status'], 200, '测试失败')

    def test06(self):  # 查询ID为2040的用户
        ss = self.jzt_api.login('15123901004', '123456')
        token = self.jzt_api.get_token(ss, 'token_name')
        test06 = self.jzt_api.my_home('2040', token)
        self.assertEqual(test06['status'], 200, '测试失败')


if __name__ == '__main__':
    unittest.main()

# import time
#
#
# def all_case():
#     case_dir = 'G:\\APP\\Jzt_api'  # 存放测试用例文件的目录
#     testcase = unittest.TestSuite()  # 构造测试集
#     discover = unittest.defaultTestLoader.discover(case_dir, pattern='test*.py',
#                                                    top_level_dir=None)  # 使用discover方法筛选出测试用例
#     for test_suit in discover:  # 循环添加到测试套件中
#         for test_case in test_suit:
#             testcase.addTest(test_case)
#     print(testcase)
#     return testcase
#
#
# if __name__ == '__main__':
#     now = time.strftime("%Y-%m-%d %H_%M_%S")
#     uli = 'G:\\APP\\Jzt_api\\' + now + '.html'
#     fp = open(uli, 'wb')
#     runner = HTMLTestRunner(stream=fp, title='金智塔接口测试报告', description='测试用例执行情况：')
#     runner.run(all_case())  # run所有测试用例
#
#
# def test011():
#     print('测试用例是否执行')
