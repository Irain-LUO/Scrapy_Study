# -*- coding: utf-8 -*-
import scrapy
from choushibaike.items import ChoushibaikeItem
class SpiderChoushibaikeSpider(scrapy.Spider):
    name = 'spider_csbk'   #  爬虫名称
    allowed_domains = ['qiushibaike.com']  #  限定爬取该域名下的内容
    start_urls = ['https://www.qiushibaike.com/text/page/1/']  # 访问请求开始
    base_domain = "https://www.qiushibaike.com"   #   补充下一页的域名
    def parse(self, response):
        print("$" * 20)
        duanzidivs = response.xpath("//div[@class='col1 old-style-col1']/div")   #   SelectorList
        for duanzidiv in duanzidivs:            #  Selector
            author = duanzidiv.xpath(".//h2/text()").get().strip()  #  爬取段子的作者
            content = duanzidiv.xpath(".//div[@class='content']//text()").getall()  # 爬取一个段子所有内容
            content = "".join(content).strip()   #  转换为json形式，去掉字符串两边的空格
            item = ChoushibaikeItem(author= author, content= content)   #  固定传参数量、以类的形式传参（不是字典）
            yield  item
        next_url = response.xpath("//*[@id='content']/div/div[2]/ul/li[last()]/a/@href").get()  #  获取下一页url
        if not next_url: #   判断是否有下一页
            return  #  没有下一页返回为空
        else:
            yield  scrapy.Request(self.base_domain + next_url, callback=self.parse)
            #  有下一页，继续爬取。类似递归思路，直到没有为止。
        print("$" * 20)


        # pass
