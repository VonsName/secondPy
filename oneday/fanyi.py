# __author:  Administrator
# __date:  2019/5/13/013
from oneday import jsone

import requests

data = {
    "query": "人生库存",
    "from": "zh",
    "to": "en",
    "transtype": "translang",
    "simple_means_flag": "3",
    "sign": "801673.579768",
    "token": "599951726e2a1bda90363f86d55e8515"
}
headers = {"user-agent":
               "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36"}
url = "https://fanyi.baidu.com/v2transapi"
res = requests.post(url, data=data, headers=headers)

dict_res = jsone.loads(res.content.decode())

print(dict_res)
