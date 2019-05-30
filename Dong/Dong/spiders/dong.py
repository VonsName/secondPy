# -*- coding: utf-8 -*-
import scrapy
from Dong.items import DongItem


class DongSpider(scrapy.Spider):
    name = 'dong'
    allowed_domains = ['bbs.sun0769.com']
    start_urls = ['http://bbs.sun0769.com/portal.php']

    def parse(self, response):
        li_list = response.xpath("//div[@class='newsList1']//li")
        for li in li_list:
            item = DongItem()
            item["desc_url"] = li.xpath("./a/@href").extract_first()
            item["desc"] = li.xpath("./a/text()").extract_first()
            next_url = item["desc_url"]
            if next_url is not None:
                yield scrapy.Request(
                    next_url,
                    callback=self.parse_details,
                    meta={"item": item}
                )

    def parse_details(self, response):
        details = response.xpath("//div[@id='postlist']//td[@class='t_f']/text()").extract()
        item = response.meta["item"]
        item["details"] = details
        yield item
