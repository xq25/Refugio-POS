import json
from model.Products import Products
from service.ProductsService import ProductService as Ps

class Beers(Products):#corregir toda la clase
    def __init__(self, name, price, file, items, color:str, profile:str, type = "BR", id = Ps.assingId("BR")):
        super().__init__(id, name, price, type, file, items)
        self.__color = color #Tipo de cerveza (Roja, Negra, Dorada)
        self.__profile = profile # Se centra principalmente en (Dulce, Amargo, Aroma, Etc)

    def fromJson(jsonData):
        info = json.loads(jsonData)
        Beers(info.get("name"), info.get("price"),info.get("file"),info.get("items"), info.get("color"), info.get("profile"))

    def toJson(self):
        return {"id": self._id,
                "name": self._name,
                "price": self._price,
                "type": self._type,
                "file": self._file,
                "items" : self._items,
                "color" : self.getColor(),
                "profile" : self.getProfile()}
    
    # --- Accesores y Mutadores ---
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
    def setType(self, newType):
        super().setType(newType)

    def getFile(self):
        return self._file
    def setFile(self, newFile):
        super().setFile(newFile)

    def getItems(self):
        return self._items
    def setItems(self, newDict):
        super().setItems(newDict)

