# # __author:  Administrator
# # __date:  2019/5/24/024
#
#
#
#
# class TieBaSpider:
#     def __init__(self, tieba_name):
#         self.start_url = "https://tieba.baidu.com/mo/q/m?kw=" + tieba_name + "&pn=0"


import requests
from pprint import pprint
from lxml import etree
import re

headers = {"user-agent":
               "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36"}

# https://tieba.baidu.com/mo/q/m?kw=梦幻西游&pn=0&lp=5024&forum_recommend=1&lm=0&cid=0&has_url_param=0&pn=250&is_ajax=1
res = requests.get(
    "https://tieba.baidu.com/mo/q/m?kw=梦幻西游&pn=0&lp=5024&forum_recommend=1&lm=0&cid=0&has_url_param=0&pn=250&is_ajax=1",
    headers=headers)

dict_c = res.content.decode("utf-8")
print(dict_c)
cont = re.findall("content(.*)", dict_c, re.DOTALL)
print(cont)


# dict_s = {"no": 0, "data": {"num": "1"}}
# print(dict_s["data"]["num"])
# print(headers["user-agent"])
