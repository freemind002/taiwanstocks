from Cnyes.cnyesEnum import InputType

class factory:
    def getInstance(self,t):
        if t == InputType.mongodb:
            from Cnyes.mongodb import database
            return database()
        elif t == InputType.mysql:
            from Cnyes.mysqldb import database
            return database()
        elif t == InputType.csv:
            from Cnyes.csvStore import database
            return database()
        else:
            return None