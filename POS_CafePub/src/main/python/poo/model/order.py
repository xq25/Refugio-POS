from helpers import utils
import json

class Order():
    def __init__(self, productList:list, id = utils.randomString(5)):
        self.__productList = productList
        self.__id = id
    
    @staticmethod
    def fromJson(jsonData):
        info = json.dumps(jsonData)
        Order(info.get("products"))

    def toJson(self):
        return {"id": self.__id,
                "products" : self.__productList}

    def getId(self):
        return self.__id
    
    def getProductList(self):
        return self.__productList
    def setProductList(self, newProductList):
        self.__productList = newProductList
        