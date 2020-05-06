# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import  json
#
# class ChoushibaikePipeline(object):
#     def __init__(self):
#         self.fp = open("duanzi.json","w",encoding='utf-8')   # 管道类初始化，以w打开文件
#
#     def open_spider(selfs,spider):    # 爬虫开始钱，执行
#         print('开始了')
#
#     def process_item(self, item, spider):    # 爬虫开始过程，执行
#         item_json = json.dumps(dict(item),ensure_ascii=False)  # ensure_ascii=False:以中文字符保存
#         self.fp.write(item_json + '\n')
#         return item
#
#     def close_spider(self,spider):    # 爬虫结束后，执行
#         self.fp.close()
#         print("over")

import json
# from scrapy.exporters import JsonItemExporter   #  JsonItemExporter：一次性写入大量数据，占用内存
# #   sonLinesItemExporter：一个字典一行，不满足json格式的；数据都直接存到磁盘文件中，内存占用少.
# class ChoushibaikePipeline(object):
#     def __init__(self):
#         self.fp = open("duanzi.json","wb")   # 管道类初始化，以wb二进制打开文件，二进制没有编码形式
#         # ensure_ascii=False:以中文字符保存
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
#         self.exporter.start_exporting()  # 以标识 exporting 过程的开始。
#
#     def open_spider(selfs,spider):    # 爬虫开始前，执行
#         print('开始了')
#
#     def process_item(self, item, spider):    # 爬虫开始过程，执行
#         self.exporter.export_item(item)      # 爬虫获取到的每项item数据的处理方法
#         return item
#
#     def close_spider(self,spider):    # 爬虫结束后，执行
#         self.exporter.finish_exporting()    #  以标识 exporting 过程的结束。
#         self.fp.close()
#         print("over")


from scrapy.exporters import JsonLinesItemExporter
#   JsonLinesItemExporter：一个字典一行，不满足json格式的；数据都直接存到磁盘文件中，内存占用少.
class ChoushibaikePipeline(object):
    def __init__(self):
        self.fp = open("duanzi.json","wb")   # 管道类初始化，以wb二进制打开文件，二进制没有编码形式
        # ensure_ascii=False:以中文字符保存
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
    def open_spider(selfs,spider):    # 爬虫开始前，执行
        print('开始了')
    def process_item(self, item, spider):    # 爬虫开始过程，执行
        self.exporter.export_item(item)      # 爬虫获取到的每项item数据的处理方法
        return item
    def close_spider(self,spider):    # 爬虫结束后，执行
        self.fp.close()   #   关闭文件
        print("over")