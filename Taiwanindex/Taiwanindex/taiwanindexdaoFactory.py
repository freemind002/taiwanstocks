from Taiwanindex.taiwanindexEnum import InputType

class factory:
    def getInstance(self,t):
        if t == InputType.mongodb:
            from Taiwanindex.mongodb import database
            return database()
        elif t == InputType.mysql:
            from Taiwanindex.mysqldb import database
            return database()
        elif t == InputType.csv:
            from Taiwanindex.csvStore import database
            return database()
        else:
            return None