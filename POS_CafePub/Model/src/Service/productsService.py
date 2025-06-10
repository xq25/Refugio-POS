from Model.src.Helpers import utils
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
    else:
        raise ("No existe este tipo de producto")
    
    id = type + utils.orderId(num)
    return id

def idValidation(id):
    if len(id) != 5:
        raise ("Id invalida")
    return True
    