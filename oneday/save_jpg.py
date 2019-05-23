# __author:  Administrator
# __date:  2019/5/14/014

import requests

# res = requests.get("https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=3300305952,1328708913&fm=27&gp=0.jpg")
#
# # wb:写二进制
# with open("ma.jpg", "wb") as f:
#     f.write(res.content)

res = requests.get("http://www.baidu.com")
res.encoding = "utf-8"
print(res.text)
print(res.content.decode())
