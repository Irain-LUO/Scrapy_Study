# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem
class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'  #  爬虫名字
    allowed_domains = ['wxapp-union.com']   #  网站域名
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=11']  # 起始网页
    rules = (
        #  allow:需要爬取的网页； follow:是否继续爬取下一页
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=11'), follow=True),
        #  callback:提取详情网页内容
        #   follow=False: 防止重复爬取。因为：在详情网页中出现其他符合爬取规格的网页。
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback="parse_detail", follow=False),
    )
    def parse_detail(self, response):   #  爬取详情网页
        # fp = open("wx.json", "wb")
        # fp.close()  #  爬虫结束后，关闭文件
        title = response.xpath("//*[@id='ct']/div[1]/div/div[1]/div/div[2]/div[1]/h1/text()").get()  #  提起文章标题
        author = response.xpath("//p[@class='authors']//a/text()").get()  #  提起作者
        time = response.xpath("//*[@id='ct']/div[1]/div/div[1]/div/div[2]/div[3]/div[1]/p/span/text()").get()  #  提起发表时间
        content = response.xpath("//td//text()").getall()  #  提起文章内容
        content = "".join(content).strip()  #  list类型转换为字符型
        item = WxappItem(title=title, author=author, time=time, content=content)  #  传参
        yield item  #  item传给管道pipelines

        print("=" * 40)
        print(item)

        print("=" * 40)
