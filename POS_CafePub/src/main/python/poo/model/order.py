from helpers import utils
import json

class Order():
    #productList es una lista de jsons que contiene las siguientes keys (idProducto, nombreProducto, cantidad y precio)
    def __init__(self, productList:list, id = utils.randomString(5)):
        self.__productList = productList  #[{},{},{},{}]
        self.__costo = None #El costo lo definimos cuanto se vaya a cancelar el pedido
        self.__id = id
    
    @staticmethod
    def fromJson(jsonData:dict):
        info = json.dumps(jsonData)
        Order(info.get("products"))

    def toJson(self):
        return {"id": self.__id,
                "products" : self.__productList}

    def getId(self):
        return self.__id
    
    def getProductList(self):
        return self.__productList
    def setProductList(self, newProductList:list):
        self.__productList = newProductList
        