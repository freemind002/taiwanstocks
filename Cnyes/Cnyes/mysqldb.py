import pymysql
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
        config = {'host':'127.0.0.1',
                  'port':3306,
                  'user':'root',
                  'password':'a123456',
                  'db':'cnyesdb',}
        self.__connection = pymysql.connect(**config)
    def _Save__isExist(self,name):
        with self.__connection.cursor() as cursor:
            cursor.execute('show tables;')
            result = cursor.fetchall()
            if [i for i in result if name in i]:
                return True
            return False
    def _Save__createTable(self,name):
        with self.__connection.cursor() as cursor:
            sql = "create table %s(date varchar(30),open_price decimal(7,2),high_price decimal(7,2),low_price decimal(7,2),close_price decimal(7,2),volume decimal(7,2));" % name
            try:
                cursor.execute(sql)
            except Exception as e:
                logging.info(e)
                cursor.rollback()
                return False
            else:
                logging.info("create table %s"%name)
                self.__connection.commit()
                return True
    def _Save__deDuplicate(self,item):
        with self.__connection.cursor() as cursor:
            cursor.execute('select * from %s where date="%s"'%(item['category'],item['date']))
            result = cursor.fetchall()
        if [i for i in result if item['date'] in i]:
            return True
        return False
    def insert(self,item):
        if not self._Save__isExist(item['category']):
            result = self._Save__createTable(item['category'])
            if not result:
                return False
        with self.__connection.cursor() as cursor:
            if self._Save__deDuplicate(item):
                return False
            sql = 'insert into %s values("%s","%s","%s","%s","%s","%s")'%tuple(item.getList())
            try:
                cursor.execute(sql)
            except Exception as e:
                logging.info(e)
                self.__connection.rollback()
            else:
                logging.info("insert data:%s success"%item['date'])
                self.__connection.commit()
                return True
    def close(self):
        self.__connection.close()
