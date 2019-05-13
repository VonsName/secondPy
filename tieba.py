# __author:  Administrator
# __date:  2019/5/13/013


# headers = {"User-Agent":
#                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
# url = "http://tieba.baidu.com/f?"
# param = {"kw": "帝吧", "pn": "100"}
# response = requests.get(url, headers=headers, params=param)
# print(response.status_code)
# print(response.text)
import requests


class TieBaSpider:
    def __init__(self, tieba_name):
        self.url = "http://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {"User-Agent":
                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"}
        self.tieba_name = tieba_name

    def get_url_list(self):
        # url_list = []
        # for i in range(1000):
        #     url_list.append(self.url.format(i * 50))
        # return url_list
        return [self.url.format(i * 50) for i in range(1000)]

    def parse_url(self, url):  # 请求url
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_content(self, content, page_num):  # 存储文件
        file_path = "{}吧-第{}页.html".format(self.tieba_name, page_num)

        # encoding 这里要添加这个参数 否则在f.write(content)的时候会报编码错误
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            content = self.parse_url(url)
            page_num = url_list.index(url) + 1  # url_list.index(url)->取url在url_list的下标位置
            self.save_content(content, page_num)


if __name__ == '__main__':
    tieBa_spider = TieBaSpider("lol")
    tieBa_spider.run()
