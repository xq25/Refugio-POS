from helpers import utils
from service.Service import Service


class ProductService(Service):
    @staticmethod
    def add(productData):
        data = utils.getDataBaseProducts()

        #clasificamos el tipo de producto
        try: 
            key = ProductService.clasificator(productData.get("type"))
            specificData = data[f"{key}"] #specificData es la base de datos segun la clasificacion de la instacia a la que se hafce referencia
            specificData.append(productData) 
            data[f"{key}"] = specificData

            utils.safetysave("./Data/products.json", data)

        except ValueError as error:
            raise error
    
    @staticmethod
    def assingId(type:str):
        dataBase = utils.getDataBaseProducts()
        key = ProductService.clasificator(type)
        size = str(len(dataBase.get(f"{key}")) + 1)
        id = type + utils.orderId(size)
        return id
    
    # --- Validaciones --- ✅❌

    @staticmethod
    def idValidation(id:str):
        if len(id) != 5:
            raise ValueError("ID invalida, la ID del prodcuto debe tener un tamaño de 5 caracteres")
        
        if utils.stringValidation(id):
            return True

    @staticmethod 
    def nameValidation(name:str):
        if len(name)<3:
            raise ValueError("El tamaño minimo del nombre del producto es de 3 caracteres")
        if utils.stringValidation(name):
            return True

    @staticmethod
    def priceValidation(price:int):
        if  not isinstance (price,int):
            raise ValueError("El precio debe estar en pesos colombianos y debe ser ingresado en valor numerico entero")
        return True

    @staticmethod
    def itemsValidation(items:dict):
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
