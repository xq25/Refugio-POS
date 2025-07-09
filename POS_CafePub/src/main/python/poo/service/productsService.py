from helpers import utils
from service.service import Service
from service.usersService import UserService


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
    def add(productData:dict)->dict:
        data = utils.getDataBase("./Data/products.json")

        #clasificamos el tipo de producto
        try: 
            jsonCorrection = ProductService.dataToAddOk(productData)
            key = ProductService.clasificator(productData.get("type"))
            specificData = data.get(f"{key}") #specificData es la base de datos segun la clasificacion de la instacia a la que se hafce referencia
            specificData.append(productData) 
            data[key] = specificData

            utils.safetysave("./Data/products.json", data)
            return {"status" : "succcess", "message" : "Se agrego el producto con exito!", "data": jsonCorrection}

        except ValueError as error:
            raise error
    
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
    def update(id:str, newJsonData:dict)->dict:
        #Primera prueba sin realizar validaciones en esta parte del service y sin validar los privilegios del usuario
        data = utils.getDataBase("./Data/products.json")
        indexUpdate = ProductService.getIndexProductId(id) 
        key = ProductService.clasificator(id[:2])
        specificData = data.get(f"{key}")

        specificData[indexUpdate] = newJsonData 
        data[f"{key}"] = specificData

        utils.safetysave("./Data/products.json", data)
        return {"status": "success", "message": f"Se actualizo el producto {id} con exito!", "data" : newJsonData}

    @staticmethod
    def assingId(type:str)->str:
        dataBase = utils.getDataBase("./Data/products.json")
        key = ProductService.clasificator(type)
        size = str(len(dataBase.get(f"{key}")) + 1)
        id = type + utils.orderId(size)
        return id
    
    # --- Validaciones --- ✅❌

    @staticmethod
    def dataToAddOk(jsonData:dict)->dict:
        if "id" not in jsonData :
            jsonData["id"] = ProductService.assingId(jsonData.get("type"))
        try:
            ProductService.idValidation(jsonData.get("id"))
            ProductService.nameValidation(jsonData.get("name"))
            ProductService.priceValidation(jsonData.get("price"))
            
            if "items" in jsonData:
                ProductService.itemsValidation(jsonData.get("items"))

            return jsonData
        
        except ValueError as e:
            raise e

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
        if not isinstance(items, dict):
            raise ValueError("El formato de carga debe ser un diccionario o un json")

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