import json
from model.products import Products
from helpers import utils
from model.mixers import Mixers

class Cocktails(Products):
    def __init__(self,id:str,  name:str, price:int, items:dict, principal:str, mixer:Mixers, infusion:bool, type="CT"):
        super()._init_(id,name, price, type, items)

        if utils.stringValidation(principal):
            self.__principal = principal.capitalize() #Licor predominante en el coctel (principal)

        self.__mixer = Cocktails.mixerClasificator(mixer)

        if utils.boolValidation(infusion):
            self.__infusion = infusion #Tiene o no tiene alguna infusion

    @staticmethod
    def fromJson(jsonData)->object:
        info = json.loads(jsonData)
        return Cocktails(info.get("id"), info.get("name"), info.get("price"), info.get("items"), info.get("file"), info.get("principal"), info.get("mixer"), info.get("infusion"))

    def toDict(self):
        return {"id": self._id,
                "name": self._name,
                "price": self._price,
                "type": self._type,
                "principal": self.getPrincipal(),
                "mixer": self.getMixer().value, 
                "infusion" : self.getHasInfusion(),
                "items": self._items}
    
    #Accesores y Mutadores
    def getPrincipal(self):
        return self.__principal
    def setPrincipal(self, newPrincipal:str):
        if utils.stringValidation(newPrincipal):
            self.__principal = newPrincipal.capitalize()
    
    def getMixer(self):
        return self.__mixer
    def setMIxer(self, newMixer:Mixers):
        self.__mixer = Cocktails.mixerClasificator(newMixer)

    def getHasInfusion(self)->bool:
        return self.__infusion 
    def setHasInfusion(self, newValue):
        if utils.boolValidation(newValue):
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

    def getItems(self):
        return self.__items
    def setItems(self, newDict):
        super().setItems(newDict)

    @staticmethod 
    def mixerClasificator(mixer):
        if isinstance(mixer, str):
            try:
                value = Mixers(mixer)
            except ValueError:
                raise ValueError(f"{mixer} no existe dentro de la lista de mezcladores validos!")
        elif isinstance(mixer, Mixers):
            value = mixer
        else:
            raise ValueError("Ingresa un CoctailMixer Valido!")
        


    