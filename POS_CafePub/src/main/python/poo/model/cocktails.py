import json
from model.products import Products
from helpers import utils
from model.mixers import Mixers

class Cocktails(Products):
    def __init__(self,id,  name, price,  file, principal:str, mixers:list, infusion:bool, items:dict, type="CT"):
        super()._init_(id,name, price, type, file)
        self.__items = items #Diccionario con las cantidades de productos que lleva cada producto

        if utils.stringValidation(principal):
            self.__principal = principal #Licor predominante en el coctel (principal)

        self.__mixers = mixers 
        if utils.boolValidation(infusion):
            self.__infusion = infusion #Tiene o no tiene alguna infusion

    @staticmethod
    def fromJson(jsonData):
        info = json.loads(jsonData)
        Cocktails(info.get("id"), info.get("name"), info.get("price"), info.get("file"), info.get("principal"), info.get("base"), info.get("infusion"),info.get("items"))

    def toJson(self):
        return {"id": self._id,
                "name": self._name,
                "price": self._price,
                "type": self._type,
                "file": self._file,
                "principal": self.getPrincipal(),
                "base": self.getBase(), 
                "infusion" : self.getHasInfusion(),
                "items": self.getItems()}
    
    #Accesores y Mutadores
    def getPrincipal(self):
        return self.__principal
    def setPrincipal(self, newPrincipal):
        self.__principal = newPrincipal
    
    def getBase(self):
        return self.__mixers
    def setBase(self, newMixers:list):
        self.__mixers = newMixers

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

    def getFile(self):
        return self._file
    def setFile(self, newFile):
        super().setFile(newFile)

    def getItems(self):
        return self.__items
    def setItems(self, newDict):
        self.__items = newDict


    