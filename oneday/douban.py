# __author:  Administrator
# __date:  2019/5/22/022

import json
import re
from pprint import pprint

import requests

# type=tv&tag=%E7%BE%8E%E5%89%A7&sort=recommend&page_limit=20&page_start=20
url = "https://movie.douban.com/j/search_subjects"
# https://movie.douban.com/j/search_subjects?type=tv&tag=美剧&sort=recommend&page_limit=20&page_start=20
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36"}


class DouBan:
    def __init__(self, page_limit, page_start, types, tag, sort):
        self.page_limit = page_limit
        self.page_start = page_start
        self.types = types
        self.tag = tag
        self.sort = sort
        # self.url = "https://movie.douban.com/j/search_subjects?page_limit=" + self.page_limit + "&page_start=" + \
        #            self.page_start + "&type=" + self.types + "&tag=" + self.tag
        # "&sort=" + sort

        self.url = "https://movie.douban.com/j/search_subjects?page_limit={}&page_start={}&type={}&tag={}&sort={}"

    def start(self):
        self.url = self.url.format(self.page_limit, self.page_start, self.types, self.tag, self.sort)
        # self.url.format(self.page_limit, self.page_start, self.types, self.tag, self.sort)
        res = requests.get(self.url, headers=headers)
        # pprint(res.content.decode())
        # pprint(json.loads(res.content.decode(), encoding="utf-8"))
        # json.loads() 把JSON类型转为python类型
        ret = json.loads(res.content.decode(), encoding="utf-8")
        with open("data.json", "w", encoding="utf-8") as f:
            # json.dumps() 把python类型转为JSON类型
            # f.write(json.dumps(ret, ensure_ascii=False, indent=2))
            # 直接从文件描述符写出JSON数据
            json.dump(ret, f, ensure_ascii=False, indent=3)
        # json.dump(f,)
        with open("data.json", "r", encoding="utf-8") as f:
            # json.load(f) 直接从文件描述符读取json为python类型
            # ret4 = json.load(f)
            red = f.read()
            ret4 = json.loads(red, encoding="utf-8")
            pprint(ret4)


if __name__ == '__main__':
    num = 0
    douban = DouBan(20, num, "tv", "美剧", "recommend")
    douban.start()

    # str1 = "https://movie.douban.com/j/search_subjects?page_limit={}&page_start={}&type={}&tag={}&sort={}"
    # str2 = str1.format(20, num, "tv", "美剧", "recommend")
    #
    # print(str2)
