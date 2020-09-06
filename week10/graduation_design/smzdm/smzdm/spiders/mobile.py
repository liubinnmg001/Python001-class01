import scrapy
from scrapy.selector import Selector
from smzdm.items import SmzdmItem
from snownlp import SnowNLP
from datetime import datetime, timedelta
import re

class MobileSpider(scrapy.Spider):
    name = 'mobile'
    allowed_domains = ['www.smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/']

    def start_requests(self):
        url = 'https://www.smzdm.com/fenlei/zhinengshouji/h5c4s0f0t0p1/#feed-main/'
        try:
            yield scrapy.Request(url=url, callback=self.parse)
        except Exception as e:
            print(e)

    # 解析函数
    def parse(self, response):
        try:
            for number in range(1,11):
                url = Selector(response=response).xpath(f'//*[@id="feed-main-list"]/li[{number}]/div/div[2]/h5/a/@href').extract_first().strip()                                         
                yield scrapy.Request(url=url, callback=self.parse2)
        except Exception as e:
            print(e)

    def inputime(self, time_d, time_t, input_time):
        if "分钟" in time_t:
            m = re.sub('\D','',time_t)
            input_time = datetime.now() + timedelta(minutes=-int(m)) 
        elif "小时" in time_t:
            h = re.sub('\D','',time_t)
            input_time = datetime.now() + timedelta(hours=-int(h))
        return input_time.strftime('%Y-%m-%d %H:%M:%S')

    def parse2(self, response):     
        item = SmzdmItem()          
        html = Selector(response=response)
        messages = html.xpath('//*[@id="commentTabBlockNew"]/ul[1]/li[@class="comment_list"]')
        global page_max
        global ID
        page_max = 0
        ID = 0

        for message in messages:

            #手机名字
            name = message.xpath('//*[@id="feed-main"]/div[2]/div/div[1]/h1/text()').extract_first().strip()
            
            #录入时间
            time_d = message.xpath('./div[2]/div[1]/div[1]/meta/@content').extract_first()
            time_t = message.xpath('./div[2]/div[1]/div[1]/text()').extract_first()
            input_time = datetime.now()
            #评论内容
            message_r = message.xpath('./div[2]/div[3]/div[1]/p/span/text()').extract_first()
            if not message_r:
                message_r = message.xpath('./div[2]/div[2]/div[1]/p/span/text()').extract_first()

            #情感分析
            message_s = SnowNLP(message_r).sentiments

            item['name'] = name
            item['input_time'] = self.inputime(time_d, time_t, input_time)
            item['comment'] = message_r
            item['sentiments'] = float(message_s)
            yield item
        #翻页功能
        pagedown = html.xpath('//*[@id="commentTabBlockNew"]/ul[2]/li[@class="pagedown"]').extract_first()
        if pagedown:
            #页码最大值
            urlall = html.xpath('//*[@id="commentTabBlockNew"]/ul[2]/li/a/@href').extract()
            urllist = []
            for url in urlall:
                url_m = re.findall('p\d+', url)
                if url_m:
                    urllist.append(int(re.sub('p', '', url_m[0])))
            urllist.sort(reverse=True)
            page_max = urllist[0]

            #用户ID号 
            for url in urlall:
                url_m = re.findall('p/\d+', url)
                if url_m:
                    ID = int(re.sub('p/', '', url_m[0]))
                    break

        for i in range(2, page_max+1):
            url_con = f'https://www.smzdm.com/p/{ID}/p{i}/#comments'
            yield scrapy.Request(url=url_con, meta={'item': item}, callback=self.parse3)  

    def parse3(self, response):
        item = response.meta['item']               
        html = Selector(response=response)
        messages = html.xpath('//*[@id="commentTabBlockNew"]/ul[1]/li[@class="comment_list"]')
        for message in messages:

            #手机名字
            name = message.xpath('//*[@id="feed-main"]/div[2]/div/div[1]/h1/text()').extract_first().strip()
            
            #录入时间
            time_d = message.xpath('./div[2]/div[1]/div[1]/meta/@content').extract_first()
            time_t = message.xpath('./div[2]/div[1]/div[1]/text()').extract_first()
            input_time = datetime.now()
            #评论内容
            message_r = message.xpath('./div[2]/div[3]/div[1]/p/span/text()').extract_first()
            if not message_r:
                message_r = message.xpath('./div[2]/div[2]/div[1]/p/span/text()').extract_first()

            #情感分析
            message_s = SnowNLP(message_r).sentiments

            item['name'] = name
            item['input_time'] = self.inputime(time_d, time_t, input_time)
            item['comment'] = message_r
            item['sentiments'] = float(message_s)
            yield item 