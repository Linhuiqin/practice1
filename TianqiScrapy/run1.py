from scrapy import cmdline
#这个是把命令行中执行的内容搬到程序里
cmdline.execute("scrapy crawl tianqiSpider -s LOG_ENABLED=False".split())
#在命令行中执行scrapy crawl mySpider -s LOG_ENABLED=False这句，就是执行了myspider中的爬虫程序内容，后半段的参数是不显示调试信息

http://39.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112407347778641236851_1694368899232&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1694368899233
http://26.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112404141116064002086_1694369117704&pn=2&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152&_=1694369117709
jQuery112408975079038890372_1694369313668