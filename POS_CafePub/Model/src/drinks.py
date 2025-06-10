import json
from Model.src.products import Products #clase madre
from Model.src.Service import productsService as Ps

class Drinks(Products):
    

    def __init__(self,name:str, price:int, file:str, hot:bool, base, items, type = "DK", id = Ps.assingId("DK")):
        super().__init__(id, name, price, type, file, items)
        self.__hot = hot
        self.__base = base #Se refiere a la base de la bebida (Leche o Agua)

    def fromJson (jsonData):
        info = json.loads(jsonData)
        Drinks(info.get("name"), info.get("price"),info.get("file"),info.get("hot"),info.get("base"), info.get("items"))
    
    def toJson(self):
        return {"id": self._id,
                "name": self._name,
                "price": self._price,
                "type": self._type,
                "file": self._file,
                "hot": self.getIsHot(),
                "base": self.getBase()}
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



    

