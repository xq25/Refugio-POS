import json
from model.products import Products #clase madre
from helpers import utils

class Foods(Products):
    def __init__(self, id, name:str, price:int,  file:str, principal:str, sweet:bool, items:dict,  type = "FD"):
        super().__init__(id,name, price, type, file)
        if Products.itemsValidation(items):
            self.__items = items
        if utils.stringValidation(principal):
            self.__principal = principal   #Elemento principal de esa comida
        if utils.boolValidation(sweet):
            self.__sweet = sweet #Comida dulce?

    @staticmethod
    def fromJson(jsonData):
        info = json.loads(jsonData)
        Foods(info.get("id"),info.get("name"),info.get("price"), info.get("file"),info.get("principal"),info.get("sweet"), info.get("items"))
    
    def toDict(self):
        return {"id": self._id,
                "name": self._name,
                "price": self._price,
                "type": self._type,
                "file": self._file,
                "principal": self.getPrincipal(),
                "sweet": self.getSweet(),
                "items": self.getItems()}
    
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

    def getItems(self):
        return self.__items
    def setItems(self, newDict):
        self.__items = newDict
