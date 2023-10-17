#这个就是我们的爬虫程序
import scrapy#scrapy这个程序包中包含request和response类
class tianqiSpider(scrapy.Spider):#任何一个爬虫程序类都必须继承于scrapy.Spider类
        name="tianqiSpider"#这是本次编写的爬虫名称

        def start_requests(self):#这个是程序的入口函数
            url="http://www.weather.com.cn/weather/101230701.shtml"#这个是爬虫程序的入口地址
            yeild scrapy.Request(url=url,callback=self.parse)#建立scrapy.Request
            #请求类，向这个类提供网页地址，爬取完成后执行默认的回调函数parse
        #上面这个入口函数也可以用start_urls的入口地址来替代：
        #start_urls=['http://127.0.0.1:5000']。入口地址可有多个，因此它是一个列表
            
        def parse(self,response):
            print(response.url)#打印网站地址
            data=response.body.decode()#response.body是网站相应的二进制数据，即网页内容
            #通过decode解码后变成字符串
            print(data)