# -*- coding: utf-8 -*-
import scrapy
from piture_car.items import PitureCarItem
class CarSpiderSpider(scrapy.Spider):
    name = 'car_spider'
    allowed_domains = ['che168.com']
    start_urls = ['https://www.che168.com/dealer/371543/35174484.html?pvareaid=100519&userpid=440000&usercid=440100']
    def parse(self, response):
        url = response.xpath("//div[@class='car-pic-list js-box-text']/a/img/@data-original").getall() #  获取汽车图片url
        url = list(map(lambda url:response.urljoin(url),url))  #  每个url添加"https:"
        yield  PitureCarItem(url=url)  #  传递
