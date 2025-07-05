from service.serviceOrder import ServiceOrder
from service.productsService import ProductService
from helpers import utils
class OrderService(ServiceOrder):
    
    def addProduct(id:str):
        #Agregar un nuevo producto al pedido
        pass
    
    def deleteProduct():
        #Eliminar el producto del pedido
        pass

    def addUnitProduct():
        #aumentar la cantidad en un producto que ya esta en el pedido
        pass

    def deleteUnitProduct():
        #Bajar la cantidad de un producto que esta en el pedido

        #Si la cantidad llega a 0, eliminarlo del pedido
        pass

    def getCosto():
        pass

    def assingId():
        return utils.randomString(5)
