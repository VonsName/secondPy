# __author:  Administrator
# __date:  2019/5/27/027

import requests
from lxml import etree


class QiuShiBaiKe:
    def __init__(self, url):
        self.url = url
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
            "Host": "www.qiushibaike.com"}

    def start(self):
        res = requests.get(self.url, headers=self.header)
        content = res.content.decode()
        qiu_shi_html = etree.HTML(content)
        # text = qiu_shi_html.xpath("//div[@class='content']/span/text()")
        href_list = qiu_shi_html.xpath("//a[contains(@href,'article')]")
        href_str_dict = {}
        for i in href_list:
            a_str = etree.tostring(i).decode("utf-8")
            # print(re.findall("href(.*)", a_str, re.DOTALL))
            href_html = etree.HTML(a_str)
            href = href_html.xpath("//a/@href")[0]
            href_content = href_html.xpath("//div[@class='content']/span/text()")
            # print(href)
            href_content = href_content[0] if len(href_content) > 0 else None
            # print(href_content)
            href_str_dict[href] = href_content
            temp_url = self.url + href
            # print(temp_url)
        print(href_str_dict)
        # content_details = requests.get(temp_url, headers=self.header)
        # print(content_details.content.decode())

        # href_str_list = []
        # for href in href_list:
        #     href_str = etree.tostring(href)
        #     strs = href_str.decode("utf-8")
        #     href_html = etree.HTML(strs)
        #     href_str = href_html.xpath("//a/@href")
        #     href_str_list.append(href_str[0])
        # # 去重
        # distinct_list = list(set(href_str_list))
        # # 排序, 保持原来的顺序不变
        # distinct_list.sort(key=href_str_list.index)
        # print(len(distinct_list))


if __name__ == '__main__':
    qiushi = QiuShiBaiKe("https://www.qiushibaike.com/text")
    qiushi.start()
