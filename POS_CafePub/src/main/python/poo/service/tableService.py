from service.service import Service
from helpers import utils
from service.orderService import OrderService

class TableService(Service):
    @staticmethod
    def getAll():
        data = utils.getDataBase("./Data/tables.json")
        specificData = data.get("tables")
        return specificData
    
    @staticmethod
    def getId(id:str):
        data = utils.getDataBase("./Data/tables.json")
        specificData = data.get("tables")
        for s in specificData:
            if s.get("id") == id:
                return s
        raise ValueError(f"No se logro encontrar la mesa con id : {id}")
    
    @staticmethod
    def add(jsonData:dict):  #Metodo para agregar una nueva mesa
        pass
        
    @staticmethod
    def delete(id:str):  #Metodo para eliminar una mesa
        pass

    @staticmethod
    def update(id:str, newJsonData):  #Metodo para editar una mesa
        pass

    @staticmethod
    def assingId()->str:
        data = utils.getDataBase("./Data/tables.json")
        size = len(data.get("tables")) #La clave que contiene a nuestra lista de mesas es "tables"
        return str(size + 1)
    
    #Validations
    @staticmethod
    def idValidation(id:str):
        if id.isdigit():  #Validemos que el id asignado es un numero dentro de un string
            if len(id)<3:
                return True
            else:
                raise ValueError("El tamaño maximo comprendido para el id de un producto es de 2")
        else:
            raise ValueError("El id de la mesa debe estar expresado unicamente en caracteres numericos enteros")


    @staticmethod
    def orderValidation(order):
        pass




    