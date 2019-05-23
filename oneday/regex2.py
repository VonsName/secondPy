# __author:  Administrator
# __date:  2019/5/23/023

import requests
import re

url = "http://www.baidu.com/f?kw=帝吧"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"}

res = requests.get(url, headers=headers)
content = res.content.decode("utf-8")
# print(content)
print(re.findall(r"<script>(.*?)</script>", content))

