import json
from Model.src.products import Products
from Model.src.Service import productsService as Ps

class Snacks(Products):

    def __init__(self, name, price, file, items, principal,sweet, type = "SK", id = Ps.assingId("SK")):
        super().__init__(id, name, price, type, file, items)
        self.__principal = principal
        self.__sweet = sweet

    def fromJson(jsonData):
        info = json.loads(jsonData)
        Snacks(info.get("name"),info.get("price"), info.get("file"),info.get("principal"),info.get("sweet"), info.get("items"))

    def toJson(self):
        return {"id": self._id,
                "name": self._name,
                "price": self._price,
                "type": self._type,
                "file": self._file,
                "principal": self.getPrincipal(),
                "sweet": self.getSweet()}
    
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