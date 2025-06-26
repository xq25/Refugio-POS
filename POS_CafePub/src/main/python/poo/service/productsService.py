from helpers import utils

def assingId(type:str):
    dataBase = utils.getDataBaseProducts()

    if type == "BR":
        num = str(len(dataBase["beers"]) +1)
    elif type == "CT":
        num = str(len(dataBase["cocktails"])+1)
    elif type == "DK":
        num = str(len(dataBase["drinks"])+1)
    elif type == "FD":
        num = str(len(dataBase["foods"])+1)
    elif type == "SK":
        num = str(len(dataBase["snacks"])+1)
    else:
        raise ValueError(f"No existe este tipo de producto: {type}")
    
    id = type + utils.orderId(num)
    return id

def clasificator(type:str)->str:
    key = ""
    if type == "BR":
        key = "beers"
    elif type == "CT":
        key = "cocktails"
    elif type == "DK":
        key = "drinks"
    elif type == "FD":
        key = "foods"
    elif type == "SK":
        key = "snacks"
    else:
        raise ValueError(f"No xiste este tipo de producto: {type}")
    
    return key
    
#Validations
def idValidation(id:str):
    specialChars = "!@#$%^&*()_+-=[]/,.{}"
    if len(id) != 5:
        raise ValueError("ID invalida, la ID del prodcuto debe tener un tamaño de 5 caracteres")
    for i in specialChars:
        if i in id:
            raise ValueError(f"El ID del producto no puede contener caracteres especiales como {i}")
    return True 

def nameValidation(name:str):
    specialChars = "!@#$%^&*()_+-=[]/,.{}"
    if len(name)<3:
        raise ValueError("El tamaño minimo del nombre del producto es de 3 caracteres")
    for i in specialChars:
        if i in name:
            raise ValueError("El nombre del producto no puede contener caracteres especiales")
    return True

def priceValidation(price:int):
    if  not isinstance (price,int):
        raise ValueError("El precio debe estar en pesos colombianos y debe ser ingresado en valor numerico entero")
    return True

def itemsValidation(items:dict):
    if not items:
        raise ValueError("Cargue la lista de elementos necesarios para realizar este producto")
    if not isinstance(items, dict):
        raise ValueError("El formato de carga debe ser un diccionario o un json")
#CRUD
def add(productData):
    data = utils.getDataBaseProducts()

    #clasificamos el tipo de producto
    try: 
        key = clasificator(productData.get("type"))
        specificData = data[f"{key}"]
        specificData.append(productData)
        data[f"{key}"] = specificData

        utils.safetysave("./Data/products.json", data)

    except ValueError as error:
        raise error

