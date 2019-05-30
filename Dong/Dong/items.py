# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DongItem(scrapy.Item):
    # define the fields for your item here like:
    desc_url = scrapy.Field()
    desc = scrapy.Field()
    details = scrapy.Field()
    pass
