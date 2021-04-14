import pymongo
import logging
from Cnyes.cnyesdao import Save

def singletonDecorator(cls,*args,**kwargs):
    instance = {}
    def wrapperSingleton(*args,**kwargs):
        if cls not in instance:
            instance[cls] = cls(*args,**kwargs)
            logging.info('new instance')
        return instance[cls]
    return wrapperSingleton

@singletonDecorator
class database(Save):
    def __init__(self):
        self.__connection = pymongo.MongoClient(host='127.0.0.1',port=27017)
        self.__db = self.__connection.cnyesdb
    def _Save__isExist(self,name):
        return True
    def _Save__createTable(self,name):
        return True
    def _Save__deDuplicate(self,item):
        collections = self.__db[item['category']]
        result = collections.find_one({'date':item['date']})
        if result:
            return True
        return False
    def insert(self,item):
        if not self._Save__deDuplicate(item):
            collections = self.__db[item['category']]
            collections.insert(item.toDict())
            logging.info("Mongo:insert data success")
            return True
        return False
    def close(self):
        self.__connection.close()
