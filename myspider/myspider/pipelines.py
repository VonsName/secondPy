# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyspiderPipeline(object):
    def process_item(self, item, spider):
        # 2个Pipeline的时候 会先经过这个Pipeline 需在settings.py里面配置
        item["hello"] = "word"
        return item


class MyspiderPipeline1(object):
    def process_item(self, item, spider):
        # print(item)
        return item
