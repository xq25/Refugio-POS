import json
from abc import ABC, abstractmethod
from service.productsService import ProductService

class Products(ABC):
    def __init__(self,id:str, name:str, price:int, type:str, file:str):
        try: 
            if ProductService.idValidation(id):
                self._id = id
            if ProductService.nameValidation(name):
                self._name = name.capitalize()
            if ProductService.priceValidation(price):
                self._price = price
        except Exception as error:
            raise error
        self._type = type
        self._file = file
        
    #Accesores y Mutadores
    @abstractmethod
    def getId(self):
        return self._id
    #Id no tiene metodo de cambiar, debido a que se asigna automaticamente referente a la base de datos

    @abstractmethod
    def getName(self):
        return self._name
    @abstractmethod
    def setName(self,newName):
        self._name = newName

    @abstractmethod
    def getPrice(self):
        return self._price
    @abstractmethod
    def setPrice(self, newPrice):
        self._price = newPrice

    @abstractmethod
    def getType(self):
        return self._type
    #No se puede cambiar el tipo de un producto despues de ya ser asignado
    
    @abstractmethod
    def getFile(self):
        return self._file
    @abstractmethod
    def setFile(self, newFile):
        self._file = newFile
