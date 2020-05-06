from scrapy import cmdline

cmdline.execute("scrapy crawl wxapp_spider".split())
# cmdline.execute(["scrapy", "crawl", 'spider_csbk'])    #  cmdline.execute("scrapy crawl spider_csbk".split())效果一样