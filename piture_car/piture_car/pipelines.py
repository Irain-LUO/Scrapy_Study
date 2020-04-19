# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib.request
class PitureCarPipeline(object):
    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'image') #  图片存储路径
        if not os.path.exists(self.path):  #  检查是否存在Image文件夹
            os.mkdir(self.path)
    def process_item(self, item, spider):
        urls = item['url'] # 提取图片url
        for url in urls:
            picture_name = url.split('_')[-1]   #  从url中获取图片名称
            urllib.request.urlretrieve(url=url,filename=os.path.join(self.path,picture_name))  #  下载图片 url和绝对路径
            print("图片存储路径")
            print(os.path.join(self.path,picture_name))
        return item
