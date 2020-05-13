
# -*- coding: utf-8 -*-
import scrapy
import json
class HeaderSpiderSpider(scrapy.Spider):
    name = 'header_spider'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        user_agent = json.loads(response.text)['user-agent'] # json加载成字典
        print('='*22)
        print(user_agent) # 打印user-agentprint('='*22)
        yield scrapy.Request(self.start_urls[0], dont_filter=True)  # 取消过滤，一个User-Agentk可以重复使用
        pass