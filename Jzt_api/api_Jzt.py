# condig = utf-8
# Author: Assert
# Date:

import requests
import jsonpath
import json


# 金智塔测试环境接口测试
class Jzt_Api:
    def __init__(self):
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

    # 提取登录接口返回值中的token
    def get_token(self, json_data, key_name):
        '''获取到json中任意key的值,结果为list格式'''
        key_value = jsonpath.jsonpath(json_data, '$..{key_name}'.format(key_name=key_name))
        # key的值不为空字符串或者为empty（用例中空固定写为empty）返回对应值，否则返回empty
        return key_value

    # 登录接口
    def login(self, phone, password):
        # 登录接口地址
        url = 'http://api-jzt.miaoshare.net/login/login'
        # 登录接口date
        payload = 'phone={}&password={}&login_type=1'.format(phone, password)
        response = requests.request("POST", url, headers=self.headers, data=payload)
        res_login = response.json()
        return res_login

    # 金智塔——我的--主页
    def my_home(self, id, Token):
        date = 'member_id={}&token_name={}'.format(id, Token[0])
        url = "http://api-jzt.miaoshare.net/personal/ucenter/d_index"
        response = requests.request("POST", url, headers=self.headers, data=date)
        # print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        return response.json()


