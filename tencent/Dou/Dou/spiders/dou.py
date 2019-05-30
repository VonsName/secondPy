# -*- coding: utf-8 -*-
import scrapy


class DouSpider(scrapy.Spider):
    name = 'dou'
    allowed_domains = ['/bbs.sun0769.com']
    start_urls = ['http:///bbs.sun0769.com/']

    def parse(self, response):
        pass
