# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import re

logger = logging.getLogger(__name__)


class DongPipeline(object):
    def process_item(self, item, spider):
        item["details"] = self.process_details(item["details"])
        logger.warning(item)
        return item

    def process_details(self, details):
        details = [re.sub(r"\r\n|\s|\t", "", d) for d in details]
        details = [d for d in details if len(d) > 0]
        return details

    # 爬虫开启的时候执行一次
    def open_spider(self, spider):
        spider.hello = "hello"

    # 爬虫关闭的时候执行一次
    def close_spider(self, spider):
        print(spider.hello, "-" * 100)
