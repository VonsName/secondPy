# -*- coding: utf-8 -*-
import scrapy
import logging

# scrapy startproject myspider 创建名为myspider的项目
# scrapy genspider vons itcast.cn 创建一个名为vons的爬虫,设置允许爬取的网站为itcast.cn
# scrapy crawl vons 启动爬虫

logger = logging.getLogger(__name__)


class VonsSpider(scrapy.Spider):
    name = 'vons'  # 爬虫名
    allowed_domains = ['itcast.cn']  # 运行爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  # 最开始请求的URL地址

    # 处理start_urls对应的响应
    def parse(self, response):
        # ret = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret)
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            # item = {"name": li.xpath(".//h3/text()").extract()[0], "title": li.xpath(".//h3/text()").extract()[0]}
            item = {"name": li.xpath(".//h3/text()").extract_first(), "title": li.xpath(".//h3/text()").extract_first()}
            logger.warning(item)
            # yield item  # 将数据传到pipelines.py
