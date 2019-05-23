# __author:  Administrator
# __date:  2019/5/14/014

import requests

# 27.154.34.146:30450
# 27.189.128.205:53281
proxy = {"http": "http://27.154.34.146:30450"}
headers = {"user-agent":
               "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36"}
url = "http://www.baidu.com"

res = requests.get(url, proxies=proxy, headers=headers)

print(res.status_code)
