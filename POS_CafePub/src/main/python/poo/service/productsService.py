from helpers import utils
from service.service import Service
from service.usersService import UserService


class ProductService(Service):
    # --- Herencia de Service --- ⚙️

    @staticmethod
    def getId(id:str)->dict:
        data = utils.getDataBaseProducts()
        type = id[:2]
        key = ProductService.clasificator(type)
        specificData = data.get(f"{key}")

        for p in specificData:
            if p.get("id") == id:
                return p
        raise ValueError(f"No se logro encontrar el producto con id: {id}")

    @staticmethod
    def add(productData:dict)->None:
        data = utils.getDataBaseProducts()

        #clasificamos el tipo de producto
        try: 
            key = ProductService.clasificator(productData.get("type"))
            specificData = data.get(f"{key}") #specificData es la base de datos segun la clasificacion de la instacia a la que se hafce referencia
            specificData.append(productData) 
            data[key] = specificData

            utils.safetysave("./Data/products.json", data)

        except ValueError as error:
            raise error
    
    @staticmethod
    def delete(id:str, currentUser:dict)->None:
        info = ProductService.getId(id)
        data = utils.getDataBaseProducts()

        if UserService.hierarchiesValidation(currentUser):
            if info:
                key = ProductService.clasificator(id[:2])
                specificData = data.get(f"{key}")
                deleteIndex = ProductService.getIndexProductId(id)  
                specificData.pop(deleteIndex)
                data[f"{key}"] = specificData

                utils.safetysave("./Data/products.json",data)
            
    @staticmethod
    def update(id:str, newJsonData:dict)->None:
        #Primera prueba sin realizar validaciones en esta parte del service y sin validar los privilegios del usuario
        data = utils.getDataBaseProducts()
        indexUpdate = ProductService.getIndexProductId(id) 
        key = ProductService.clasificator(id[:2])
        specificData = data.get(f"{key}")

        specificData[indexUpdate] = newJsonData 
        data[f"{key}"] = specificData

        utils.safetysave("./Data/products.json", data)

    @staticmethod
    def assingId(type:str)->str:
        dataBase = utils.getDataBaseProducts()
        key = ProductService.clasificator(type)
        size = str(len(dataBase.get(f"{key}")) + 1)
        id = type + utils.orderId(size)
        return id
    
    # --- Validaciones --- ✅❌

    @staticmethod
    def idValidation(id:str)->bool:
        if len(id) != 5:
            raise ValueError("ID invalida, la ID del prodcuto debe tener un tamaño de 5 caracteres")
        
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
            data = utils.getDataBaseProducts()
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