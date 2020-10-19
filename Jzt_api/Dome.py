import requests
import json
import unittest

class RunMain:
    # 当前类的第一个参数是self
    def send_get(self, url):
        res = requests.get(url=url).json()
        r = json.dumps(res, indent=2, sort_keys=True)
        return r

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        r = json.dumps(res, indent=2, sort_keys=True)
        return r

    def run_main(self, url, method, data=None):  # 把data数据默认为空，因为get不用传数据，空参数要放在有值参数后面
        res = None
        if method == 'GET':
            res = self.send_get(url)
        else:
            res = self.send_post(url, data)
        return res


