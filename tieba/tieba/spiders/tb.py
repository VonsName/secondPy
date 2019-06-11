# -*- coding: utf-8 -*-
# scrapy genspider -t crawl tb tieba.baidu.com
import logging

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

logger = logging.getLogger(__name__)


class TbSpider(CrawlSpider):
    name = 'tb'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com//f?kw=帝吧&red_tag=y1370273843']

    rules = (
        Rule(LinkExtractor(allow=r'//tieba.baidu.com/f?kw=帝吧&ie=utf-8&pn=\d+'), callback='parse_item',
             follow=True),
    )

    def parse_item(self, response):
        print("aaaaaaaaaaaaaaaa")
        item_list = response.xpath("//ul[@id='thread_list']//div[@class='threadlist_lz clearfix']//a/text()")
        logging.warning(item_list)
