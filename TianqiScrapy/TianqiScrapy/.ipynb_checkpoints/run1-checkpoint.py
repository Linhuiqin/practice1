from scrapy import cmdline#这个是把命令行中执行的内容搬到程序里
cmdline.execute("scrapy crawl tianqiSpider -s LOG_ENABLED=False".split())
#在命令行中执行scrapy crawl mySpider -s LOG_ENABLED=False这句，就是执行了myspider中的爬虫程序内容，后半段的参数是不显示调试信息