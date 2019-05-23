# __author:  Administrator
# __date:  2019/5/16/016

import sys

import requests

headers = {"user-agent":
               "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36"}
url = "http://www.baidu.com"


class BaiDuFanYi:
    def __init__(self, trans_str):
        self.trans_str = trans_str

    @staticmethod
    def run():
        requests.get(url, headers=headers)


if __name__ == '__main__':
    trans_st = sys.argv[1]
    bai_du_fan_yi = BaiDuFanYi(trans_st)
    bai_du_fan_yi.run()
