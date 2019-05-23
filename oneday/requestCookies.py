# __author:  Administrator
# __date:  2019/5/21/021

import requests
from retrying import retry

response = requests.get("http://www.baidu.com")

print(response.cookies)

dict_ = requests.utils.dict_from_cookiejar(response.cookies)
print(dict_)

# requests.utils.quote() url编码解码
# requests.utils.unquote()

res = requests.get("https://www.12306.cn/mormhweb", timeout=30)
assert res.status_code == 200


@retry(stop_max_attempt_number=3)
def retry_test():
    print("retry")


if __name__ == '__main__':
    retry_test()
