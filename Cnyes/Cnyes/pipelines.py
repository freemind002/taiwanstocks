# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from Cnyes.cnyesEnum import InputType
from Cnyes.cnyesdaoFactory import factory
import logging
from scrapy.exceptions import DropItem

fac = factory()

class MYSQLPipeline:
    def __init__(self):
        self.db = fac.getInstance(InputType.mysql)
    def process_item(self,item,spider):
        result = self.db.insert(item)
        if not result:
            raise DropItem("MYSQL: %s is duplicated"%item['date'])
        return item
    def __del__(self):
        self.db.close()
        logging.info("mysql connection close...")

class MONGOPipeline:
    def __init__(self):
        self.db = fac.getInstance(InputType.mongodb)
    def process_item(self,item,spider):
        result = self.db.insert(item)
        if not result:
            raise DropItem("Mongo: %s is duplicated"%item['date'])
        return item
    def __del__(self):
        self.db.close()
        logging.info("mogodb connection close...")

class CSVPipeline:
    def __init__(self):
        self.db = fac.getInstance(InputType.csv)
    def process_item(self,item,spider):
        result = self.db.insert(item)
        if not result:
            raise DropItem("CSV: %s is duplicated"%item['date'])
        return item



