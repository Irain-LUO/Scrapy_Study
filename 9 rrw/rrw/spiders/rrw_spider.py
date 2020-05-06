# -*- coding: utf-8 -*-
import scrapy
class RrwSpiderSpider(scrapy.Spider):
    name = 'rrw_spider'  #  爬虫名字
    allowed_domains = ['renren.com']   #  网站域名
    start_urls = ['http://renren.com/']  # 起始网页
    def start_requests(self):
        url = "http://www.renren.com/PLogin.do"  #  人人网登录url
        data = {    #  post请求数据
            "email":"13636715336",   #  账号。不管是邮箱还是手机号，都是用‘email’
            "password":"peoplepeople55"  #  密码
        }
        request = scrapy.FormRequest(url=url, formdata=data, callback=self.parse_page)  #  模拟登录人人网，成功后调用parse_page
        yield request
    def parse_page(self,response):
        url = "http://www.renren.com/974247988/profile" #  人人网个人主页
        request = scrapy.Request(url=url, callback=self.parse_profile)   #  成功访问后调用parse_profile
        yield request
    def parse_profile(self,response):
        with open('profile.html', 'w', encoding='utf-8') as  fp:   #  保存个人主页面到HTML，用浏览器打开
            fp.write(response.text)
