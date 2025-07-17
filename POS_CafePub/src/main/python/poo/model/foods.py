import json
from model.products import Products #clase madre
from helpers import utils

class Foods(Products):
    def __init__(self, id, name:str, price:int,  items:dict, principal:str, sweet:bool,  type = "FD"):
        super().__init__(id,name, price, type, items)
        
        if utils.stringValidation(principal):
            self.__principal = principal   #Elemento principal de esa comida

        if utils.boolValidation(sweet):
            self.__sweet = sweet #Comida dulce?

    @staticmethod
    def fromJson(jsonData)->object:
        info = json.loads(jsonData)
        return Foods(info.get("id"),info.get("name"),info.get("price"), info.get("items"),info.get("principal"),info.get("sweet"))
    
    def toDict(self):
        return {"id": self._id,
                "name": self._name,
                "price": self._price,
                "type": self._type,
                "principal": self.getPrincipal(),
                "sweet": self.getSweet(),
                "items": self._items}
    
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

    def getItems(self):
        return self._items
    def setItems(self, newDict):
        super().setItems(newDict)
