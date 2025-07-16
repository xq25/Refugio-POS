from helpers import utils
from service.service import Service
from service.usersService import UserService
from model.beers import Beers
from model.cocktails import Cocktails
from model.drinks import Drinks
from model.foods import Foods
from model.snacks import Snacks
from model.products import Products
import json


class ProductService(Service):
    # --- Herencia de Service --- ⚙️
    @staticmethod
    def getAll(type:str)->dict:
        data = utils.getDataBase("./Data/products.json")
        try :
            specifiData =  data.get(type)
            return {"status": "success", "message": f"Se cargo con exito la base de datos de {type}", "data" : specifiData}
        except Exception:
            raise Exception(f"no se pudo encontrar la clasificacion: {type}, dentro de la base de datos")

    @staticmethod
    def getId(id:str)->dict:
        
        data = utils.getDataBase("./Data/products.json")
        type = id[:2]
        key = ProductService.clasificator(type)
        specificData = data.get(f"{key}")
        info = None

        for p in specificData:
            if p.get("id") == id:
                info = p
        if info is not None:
            return info
        else:
            raise ValueError(f"No se logro encontrar el producto con id: {id}")

    @staticmethod
    def add(jsonData)->dict:
        data = utils.getDataBase("./Data/products.json")
        classes = [Beers, Cocktails, Drinks, Foods, Snacks]
        infoJson = json.loads(jsonData)

        #clasificamos el tipo de producto
        productClass = ProductService.clasificator(infoJson.get("type"))
        product = None
        for i in classes:
            
            if i.__name__ == productClass:
                product = i.fromJson(jsonData)

        if product is not None:

            specificData = data.get(f"{productClass}") #specificData es la base de datos segun la clasificacion de la instacia a la que se hafce referencia
            specificData.append(product.toDict()) 
            data[productClass] = specificData

            utils.safetysave("./Data/products.json", data)
            return {"status" : "succcess", "message" : "Se agrego el producto con exito!", "data": product.toDict()}
        else:
            raise TypeError("Error al instanciar el producto")

    @staticmethod
    def delete(id:str, currentUser:dict)->dict:
        productDelete = ProductService.getId(id)
        data = utils.getDataBase("./Data/products.json")

        if UserService.hierarchiesValidation(currentUser):
            if productDelete:
                key = ProductService.clasificator(id[:2])
                specificData = data.get(f"{key}")
                deleteIndex = ProductService.getIndexProductId(id)  
                specificData.pop(deleteIndex)
                data[f"{key}"] = specificData

                utils.safetysave("./Data/products.json",data)
                return {"status" : "success", "message": f"Se elimino con exito el producto {id}!", "data": productDelete}
            
    @staticmethod
    def update(id:str, newJsonData)->dict:
        classes = [Beers, Cocktails, Drinks, Foods, Snacks]
        product = None

        #Primera prueba sin realizar validaciones en esta parte del service y sin validar los privilegios del usuario
        data = utils.getDataBase("./Data/products.json")
        indexUpdate = ProductService.getIndexProductId(id) 
        key = ProductService.clasificator(id[:2])
        specificData = data.get(f"{key}")

        for i in classes:
            if i.__name__ == key:
                product = i.fromJson(newJsonData)

        if product is not None:

            specificData[indexUpdate] = product.toDict() 
            data[f"{key}"] = specificData

            utils.safetysave("./Data/products.json", data)
            return {"status": "success", "message": f"Se actualizo el producto {id} con exito!", "data" : product.toDict()}
        else:
            raise TypeError("Error al instanciar el producto con la nueva informacion")

    @staticmethod
    def assingId(type:str)->str:
        dataBase = utils.getDataBase("./Data/products.json")
        key = ProductService.clasificator(type)
        size = str(len(dataBase.get(f"{key}")) + 1)
        id = type + utils.orderId(size)
        return id
    
    # --- Validaciones --- ✅❌


    # --- Herramientas Utiles ---
    @staticmethod
    def clasificator(type:str)->str:
        key = ""
        if type == "BR":
            key = "Beers"
        elif type == "CT":
            key = "Cocktails"
        elif type == "DK":
            key = "Drinks"
        elif type == "FD":
            key = "Foods"
        elif type == "SK":
            key = "Snacks"
        else:
            raise ValueError(f"No existe este tipo de producto: {type}")
        
        return key

    @staticmethod 
    def getIndexProductId(id)->int:
        info = ProductService.getId(id)
        if info:
            data = utils.getDataBase("./Data/products.json")
            type = id[:2]
            key = ProductService.clasificator(type)
            specificData = data.get(f"{key}")

            for p, info in enumerate(specificData):
                if info.get("id") == id:
                    return p
            raise ValueError(f"Algo salio mal al momento de identificar el indice del producto con id: {id}")\
            
    @staticmethod 
    def changeTypeValidation(currentType, newType):
        if currentType != newType:
            raise ValueError("El tipo de producto no se puede cambiar")
        else:
            return True