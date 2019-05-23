# __author:  Administrator
# __date:  2019/5/14/014

import requests

url = "http://www.renren.com/PLogin.do"
data = {"email": "894611653@qq.com", "password": "bemyself0828."}
headers = {"user-agent":
               "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Mobile Safari/537.36"}
session = requests.session()

# 登录
res = session.post(url, data=data, headers=headers)
res.encoding = "utf-8"

# print(res.content.decode())
# res = session.get("http://www.renren.com/327550029/profile", headers=headers)

# with open("renren.html", "w", encoding="utf-8") as f:
#    f.write(res.content.decode())

# 字典推导式
dic = {i: i + 10 for i in range(10)}
print(dic)  # {0: 10, 1: 11, 2: 12, 3: 13, 4: 14, 5: 15, 6: 16, 7: 17, 8: 18, 9: 19}
