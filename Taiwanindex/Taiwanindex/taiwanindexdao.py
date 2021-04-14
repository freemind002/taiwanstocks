from abc import ABCMeta,abstractmethod

class Save(metaclass = ABCMeta):
    @abstractmethod
    def __isExist(self,name):
        pass
    @abstractmethod
    def __createTable(self,name):
        pass
    @abstractmethod
    def insert(self,item):
        pass
    @abstractmethod
    def __deDuplicate(self,item):
        pass