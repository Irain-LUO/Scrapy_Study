# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class ChoushibaikeItem(scrapy.Item):   #   Item中定义实例变量
    # define the fields for your item here like:
    # name = scrapy.Field()
    author = scrapy.Field()
    content = scrapy.Field()
    pass
