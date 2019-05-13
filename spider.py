# __author:  Administrator
# __date:  2019/5/13/013

import requests

headers = {"User-Agent":
               "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}

# params = {"wd": "传智博客"}
# url = "https://www.baidu.com/s?"
url = "https://www.baidu.com/s?{}".format("传智播客")
repose = requests.get(url, headers=headers)
print(repose.status_code)
print(repose.request.url)
