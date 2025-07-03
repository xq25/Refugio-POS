import json
from model.products import Products
from service.productsService import ProductService as Ps

class Snacks(Products):

    def __init__(self, name:str, price:int, file:str, principal:str,sweet:bool, type = "SK", id = Ps.assingId("SK")):
        super().__init__(id, name, price, type, file)
        self.__principal = principal.capitalize()
        self.__sweet = sweet
    
    @staticmethod
    def fromJson(jsonData):
        info = json.loads(jsonData)
        Snacks(info.get("name"),info.get("price"), info.get("file"),info.get("principal"),info.get("sweet"))

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

    def getFile(self):
        return self._file
    def setFile(self, newFile):
        super().setFile(newFile)
