# -*- coding: utf-8 -*-
import scrapy


class DongSpider(scrapy.Spider):
    name = 'dong'
    allowed_domains = ['bbs.sun0769.com']
    start_urls = ['http://bbs.sun0769.com/']

    def parse(self, response):
        pass
