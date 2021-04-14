# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#021-01-14 20:55:12 
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TaiwanindexItem(scrapy.Item):
    # define the fields for your item here like:
    # 股票名稱
    category = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # 收盤價格指數值
    close_price = scrapy.Field()
    
    def toDict(self): # 將 Item 轉為字典,方便 Mongodb 儲存
        return {k:v for k,v in self._values.items()}

    def getList(self): # 轉為列表,方便 CSV 儲存
        return [v for v in self._values.values()]
        
    def getField(self): # 獲取欄位名稱,方便 CSV 新增表頭
        return [k for k in self._values.keys()]

