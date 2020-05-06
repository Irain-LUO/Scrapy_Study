# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter #  一条一条数据存入磁盘，占用内存小
class WxappPipeline(object):
    def __init__(self):
        self.fp = open("wx.json","wb") #  二进制方式写入，不需要编码格式
        # ensure_ascii:中文字符
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
    def process_item(self, item, spider):
        self.exporter.export_item(item)  # 输出数据
        return item
    def close_spider(self,spider):
        self.fp.close()  #  爬虫结束后，关闭文件
