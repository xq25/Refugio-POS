import json
from model.products import Products
from helpers import utils

class Snacks(Products):

    def __init__(self, id, name:str, price:int, principal:str,sweet:bool, type = "SK", items = "N/A"):
        super().__init__(id, name, price, type, items)

        if utils.stringValidation(principal):
            self.__principal = principal.capitalize()

        if utils.boolValidation(sweet):
            self.__sweet = sweet
    
    @staticmethod
    def fromJson(jsonData)->object:
        info = json.loads(jsonData)
        return Snacks(info.get("id"),info.get("name"),info.get("price"),info.get("principal"),info.get("sweet"))

    def toDict(self):
        return {"id": self._id,
                "name": self._name,
                "price": self._price,
                "type": self._type,
                "principal": self.getPrincipal(),
                "sweet": self.getSweet(), 
                "items" : self._items}
    
    #Accesores y Mutadores
    def getPrincipal(self):
        return self.__principal
    def setPrincipal(self, newPrincipal):
        self.__principal = newPrincipal

    def getSweet(self):
        return self.__sweet
    def setSweet(self, newValue:bool):
        self.__sweet = newValue
    
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

        
