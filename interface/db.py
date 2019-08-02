from abc import ABC, abstractmethod 
class DB(ABC):
    @abstractmethod
    def getConnection(self):
        pass
    
    @abstractmethod
    def getDatabase(self):
        pass
    
    @abstractmethod
    def getServer(self):
        pass
    
    @abstractmethod
    def execute(self):
        pass
    
    @abstractmethod
    def getQuery(self):
        pass
    
    @abstractmethod
    def insertQuery(self):
        pass 


