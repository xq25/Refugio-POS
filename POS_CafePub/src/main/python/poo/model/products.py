import json
from abc import ABC, abstractmethod
from helpers import utils

class Products(ABC):
    def __init__(self,id:str, name:str, price:int, type:str, items:dict):
        try: 
            if Products.idValidation(id):
                self._id = id
            if Products.nameValidation(name):
                self._name = name.capitalize()
            if Products.priceValidation(price):
                self._price = price
            if Products.itemsValidation(items):
                self._items = items
                
        except Exception as error:
            raise error
        self._type = type
        
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
        if Products.nameValidation(newName):
            self._name = newName

    @abstractmethod
    def getPrice(self):
        return self._price
    @abstractmethod
    def setPrice(self, newPrice):
        if Products.priceValidation(newPrice):
            self._price = newPrice

    @abstractmethod
    def getType(self):
        return self._type
    #No se puede cambiar el tipo de un producto despues de ya ser asignado
    
    @abstractmethod
    def getItems(self):
        return self._file
    @abstractmethod
    def setItems(self, newItems):
        self._items = newItems

    @staticmethod
    def idValidation(id:str)->bool:
        if len(id) != 5:
            raise ValueError("ID invalida, la ID del producto debe tener un tamaño de 5 caracteres")
        
        if utils.stringValidation(id):
            return True

    @staticmethod 
    def nameValidation(name:str)->bool:
        if len(name)<3 and len(name) > 30:
            raise ValueError("El nombre del producto debe ser de al menos 3 caracteres y maximo 30")
        if utils.stringValidation(name):
            return True

    @staticmethod
    def priceValidation(price:int)->bool:
        if  not isinstance (price,int):
            raise ValueError("El precio debe estar en pesos colombianos y debe ser ingresado en valor numerico entero")
        return True

    @staticmethod
    def itemsValidation(items:dict)->bool:
        if not items:
            raise ValueError("Cargue la lista de elementos necesarios para realizar este producto")
        if not isinstance(items, dict) and items != "N/A":
            raise ValueError("El formato de carga debe ser un diccionario o especificar que no tiene (N/A)")
        return True
