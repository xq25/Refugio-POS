import json
from model.products import Products

class Beers(Products):
    def __init__(self, id, name:str, price:int, color:str, profile:str, type = "BR", items = "N/A"):
        super().__init__(id, name, price, type, items)
        self.__color = color #Tipo de cerveza (Roja, Negra, Dorada)
        self.__profile = profile # Se centra principalmente en (Dulce, Amargo, Aroma, Etc)

    @staticmethod
    def fromJson(jsonData)-> object:
        info = json.loads(jsonData)
        return Beers(info.get("id"),info.get("name"), info.get("price"), info.get("color"), info.get("profile"))

    def toDict(self):
        return {"id": self._id,
                "name": self._name,
                "price": self._price,
                "type": self._type,
                "color" : self.getColor(),
                "profile" : self.getProfile().capitalize,
                "items" : self._items}
    
    # --- Accesores y Mutadores ---
    def getId(self):
        return super().getId()
    
    def getColor(self):
        return self.__color
    def setColor(self, newColor):
        self.__color = newColor
    
    def getProfile(self):
        return self.__profile
    def setProfile(self, newProfile):
        self.__profile = newProfile

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
    def setItems(self, newItems):
        super().setItems(newItems)
