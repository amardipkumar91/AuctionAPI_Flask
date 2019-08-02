import config_reader
import pymongo
import sys
sys.path.append('/Users/amardip.kumar/Documents/AuctionAPI/src/interface/')
from db import *

class MongoDBException(Exception):
    pass

class MongoDB(DB):
    def __init__(self, db = None, mongourl = None):
        try:
            self.mongourl = config_reader.read("MONGODB", 'mongourl')
            self.db = config_reader.read("MONGODB", 'db')
            
        except Exception as e:
            raise MongoDBException("missing parameters")
        self.__connection = pymongo.MongoClient(self.mongourl)
        self.__cursor = self.__connection[self.db]

    def getConnection(self):
        return self.__connection
    
    def getDatabase(self):
        return self.db
    
    def getServer(self):
        return self.mongourl

    def execute(self, query = None , coll = None):
        if not coll:
            coll = 'offer'
        return self.__cursor[coll]

    def getQuery(self, query = None):
        return self.execute().find()
    
    def insertQuery(self, query= None):
        mydict = { "name": "John", "address": "Highway 37" }
        return self.execute(coll = 'offer').insert_one(mydict)

if __name__ == "__main__":
    db = MongoDB()
    abc = db.getQuery()

    for i in abc:
        print (i)
    xx = db.insertQuery()
    