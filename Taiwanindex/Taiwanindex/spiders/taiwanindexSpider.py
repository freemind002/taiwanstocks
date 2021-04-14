# -*- coding: utf-8 -*-
import scrapy
from Taiwanindex.items import TaiwanindexItem

class TaiwanindexspiderSpider(scrapy.Spider):
    name = 'taiwanindexSpider'
    allowed_domains = ['taiwanindex.com.tw']
    
    baseurl = 'https://www.taiwanindex.com.tw/index/history?'
    begin = str(input("請輸入開始日期："))
    stop = str(input("請輸入結束日期："))

    start_urls = [baseurl +
                  'id=t00' +
                  '&start=' + begin[0:4] + '%2F' + begin[4:6] + '%2F' + begin[6:] +
                  '&end=' + stop[0:4] + '%2F' + stop[4:6] + '%2F' + stop[6:]
                  ]

    def parse(self, response):
        # logging.info("into parsre function")
        stockinfos = response.xpath('//*[@id="tab2"]/div/table/tbody//tr')
        # logging.info(len(stockinfos))
        for stockinfo in stockinfos:
            item = TaiwanindexItem()
            # 股票名稱
            item['category'] = 'taiwanindexdb'
            # 日期
            item['date'] = stockinfo.xpath('./td[1]/text()').get()
            # 收盤價格指數值
            item['close_price'] = stockinfo.xpath('./td[2]/text()').get()

            yield item
