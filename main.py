
from service.mongo import *
if __name__ == "__main__":
 
    db = MongoDB()
    
    abc = db.getQuery()

    for i in abc:
        print (i)
    xx = db.insertQuery()
    