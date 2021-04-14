# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CnyesItem(scrapy.Item):
    # define the fields for your item here like:
    # stock_股票代號
    category = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # 開盤價格
    open_price = scrapy.Field()
    # 最高價格
    high_price = scrapy.Field()
    # 最低價格
    low_price = scrapy.Field()
    # 收盤價格
    close_price = scrapy.Field()
    # 成交張數
    volume = scrapy.Field()

    def toDict(self): # 將 Item 轉為字典,方便 Mongodb 儲存
        return {k:v for k,v in self._values.items()}

    def getList(self): # 轉為列表,方便 CSV 儲存
        return [v for v in self._values.values()]
        
    def getField(self): # 獲取欄位名稱,方便 CSV 新增表頭
        return [k for k in self._values.keys()]
