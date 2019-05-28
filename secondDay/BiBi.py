# __author:  Administrator
# __date:  2019/5/28/028


import requests
from pprint import pprint


class BiBi:
    def __init__(self, url):
        self.url = url

    def run(self):
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
            "Referer": "https://www.bilibili.com/v/kichiku/guide/?spm_id_from=333.11.b_7072696d6172795f6d656e75.68"}
        response = requests.get(self.url, headers=self.header)
        print(response.content.decode())


if __name__ == '__main__':
    # callback=jqueryCallback_bili_7991022552453422&
    bibi = BiBi(
        "https://api.bilibili.com/x/web-interface/newlist?rid=22&type=0&pn=1&ps=20&jsonp=jsonp&_=1559027914399")
    bibi.run()
