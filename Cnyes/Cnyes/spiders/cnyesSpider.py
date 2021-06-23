# -*- coding: utf-8 -*-
import scrapy
import time
import json
from Cnyes.items import CnyesItem

class CnyesspiderSpider(scrapy.Spider):
    name = 'cnyesSpider'
    allowed_domains = ['ws.api.cnyes.com']
    
    baseurl = 'http://ws.api.cnyes.com/ws/api/v1/charting/history?'
    symbol = input('請輸入股票代號：')
    start = input('請輸入開始日期：')
    start_year = int(str(start)[0:4])
    start_month = int(str(start)[4:6])
    start_day = int(str(start)[6:]) + 1
    to_date = int(time.mktime((start_year,start_month,start_day,0,0,0,0,0,0)))
    end = input('請輸入結束日期：')
    end_year = int(str(end)[0:4])
    end_month = int(str(end)[4:6])
    end_day = int(str(end)[6:]) + 2
    from_date = int(time.mktime((end_year,end_month,end_day,0,0,0,0,0,0)))
    
    start_urls = [baseurl +
                  'resolution=D' +
                  '&symbol=TWS:' + str(symbol) + ':STOCK' + 
                  '&from=' + str(from_date) +
                  '&to=' + str(to_date) +
                  '&quote=1']

    def parse(self, response):
        stockinfos = json.loads(response.text)
        # 日期
        dates = stockinfos['data']['t']
        # 開盤價格
        open_prices = stockinfos['data']['o']
        # 最高價格
        high_prices = stockinfos['data']['h']
        # 最低價格
        low_prices = stockinfos['data']['l']
        # 收盤價格
        close_prices = stockinfos['data']['c']
        # 成交張數
        volumes = stockinfos['data']['v']
        for date,open_price,high_price,low_price,close_price,volume in zip(dates,open_prices,high_prices,low_prices,close_prices,volumes):
            item = CnyesItem()
            # stock_股票代號
            item['category'] = 'stock_'+str(self.symbol)
            # 日期
            item['date'] = time.strftime('%Y/%m/%d', time.gmtime(date))
            # 開盤價格
            item['open_price'] = open_price
            # 最高價格
            item['high_price'] = high_price
            # 最低價格
            item['low_price'] = low_price
            # 收盤價格
            item['close_price'] = close_price
            # 成交張數
            item['volume'] = volume

            yield item

