import json
from model.products import Products #clase madre
from helpers import utils
from model.drinkBases import DrinksBases

class Drinks(Products):
    def __init__(self, id, name:str, price:int, file:str, hot:bool, base:DrinksBases, items:dict, type = "DK"):
        super().__init__(id, name, price, type, file)
        
        if Products.itemsValidation(items):   
            self.__items = items
        if utils.boolValidation(hot): 
            self.__hot = hot
        self.__base = base #Se refiere a la base de la bebida 

    @staticmethod
    def fromJson (jsonData:dict):
        info = json.loads(jsonData)
        Drinks(info.get("id"), info.get("name"), info.get("price"),info.get("file"),info.get("hot"),info.get("base"), info.get("items"))
    
    def toJson(self):
        return {"id": self._id,
                "name": self._name,
                "price": self._price,
                "type": self._type,
                "file": self._file,
                "hot": self.getIsHot(),
                "base": self.getBase(),
                "items": self.getItems()}
    #Accesores y mutadores
    def getIsHot(self):
        return self.__hot
    def setIsHot(self, newValue:bool):
        self.__hot = newValue

    def getBase(self):
        return self.__base
    def setBase(self, newBase):
        self.__base = newBase

    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
    def setName(self, newName):
        super().setName(newName)

    def getPrice(self):
        return self._price
    def setPrice(self, newPrice):
        super().setPrice(newPrice)

    def getType(self):
        return self._type

    def getFile(self):
        return self._file
    def setFile(self, newFile):
        super().setFile(newFile)

    def getItems(self):
        return self.__items
    def setItems(self, newDict):
        self.__items = newDict

    



    

