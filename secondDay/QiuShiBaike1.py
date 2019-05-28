# __author:  Administrator
# __date:  2019/5/27/027

import requests
from lxml import etree
import json
import threading


class QiuShiBaiKe1:
    def __init__(self, url):
        self.url = url
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
            "Host": "www.qiushibaike.com"}

    def run(self):
        res = requests.get(url=self.url, headers=self.header)
        c_html = etree.HTML(res.content)
        # c_html_str = etree.tostring(c_html).decode()
        href_list = c_html.xpath("//div[@class='recommend-article']//li/a/@href")
        page_num_list = c_html.xpath("//span[@class='page-numbers']/text()")
        print(page_num_list)

        # print(href_list)
        # ima_src = c_html.xpath("//div[@class='recommend-article']//li//a/img/@src")
        # print(ima_src)
        # ima_src = c_html.xpath("//div[@class='recommend-article']//li//a/img/@alt")
        # print(ima_src)
        text_list = c_html.xpath("//div[@class='recommend-article']//li//div[@class='recmd-right']/a/text()")
        # print(text_list)
        # text_href = c_html.xpath("//div[@class='recommend-article']//li//div[@class='recmd-right']/a/@href")
        # print(text_href)
        # text = c_html.xpath("//div[@class='recommend-article']//li//div[@class='recmd-right']/div/a/text()")
        # print(text)
        # content_dict = {}
        content_dict = {href: text_list[href_list.index(href)] for href in href_list}
        print(content_dict)
        with open("content.json", "w", encoding="UTF-8") as f:
            # json.dump(content_dict, f, ensure_ascii=False, indent=3)
            f.write(json.dumps(content_dict, ensure_ascii=False, indent=3))
            # for href in href_list:
            #     content_dict[href] = text_list[href_list.index(href)]

        th = threading.Thread(target=self.run())
        th.start()


if __name__ == '__main__':
    qa = QiuShiBaiKe1("https://www.qiushibaike.com/8hr/page/2/")
    qa.run()
