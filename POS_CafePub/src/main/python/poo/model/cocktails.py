import json
from model.products import Products
from service.productsService import ProductService as Ps

class Cocktails(Products):
    def __init__(self, name, price,  file, principal:str, base:str, infusion:bool, items, type="CT", id = Ps.assingId("CT")):
        super()._init_(id,name, price, type, file, items)
        self.__principal = principal #Licor predominante en el coctel (principal)
        self.__base = base #Puede ser la principal combinacion (Limon, Bretaña, Naranja)
        self.__infusion = infusion #Tiene o no tiene alguna infusion

    def fromJson(jsonData):
        info = json.loads(jsonData)
        Cocktails(info.get("name"), info.get("price"), info.get("file"), info.get("principal"), info.get("base"), info.get("infusion"),info.get("items"))

    def toJson(self):
        return {"id": self._id,
                "name": self._name,
                "price": self._price,
                "type": self._type,
                "file": self._file,
                "principal": self.getPrincipal(),
                "base": self.getBase(), 
                "infusion" : self.getHasInfusion()}
    
    #Accesores y Mutadores
    def getPrincipal(self):
        return self.__principal
    def setPrincipal(self, newPrincipal):
        self.__principal = newPrincipal
    
    def getBase(self):
        return self.__base
    def setBase(self, newBase):
        self.__base = newBase

    def getHasInfusion(self):
        return self.__infusion 
    def setHasInfusion(self, newValue):
        self.__infusion = newValue

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


    