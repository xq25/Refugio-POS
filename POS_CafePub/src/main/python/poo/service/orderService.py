from service.serviceOrder import ServiceOrder
from service.productsService import ProductService
from helpers import utils
class OrderService(ServiceOrder):

    @staticmethod
    def addProduct(order:list,idProduct:str)->list:
        #Agregar un nuevo producto al pedido
        product = ProductService.getId(idProduct)
        productFormat = OrderService.formatProductInfo(product) #La cantidad predeterminada al agregar un producto es 1
        order.append(productFormat)
        return order
    
    @staticmethod
    def deleteProduct(order:list, id:str)->list:
        index = OrderService.getIndexProductInOrder(order, id)
        order.pop(index)
        return order

    @staticmethod
    def addUnitProduct():
        #aumentar la cantidad en un producto que ya esta en el pedido
        pass

    @staticmethod
    def deleteUnitProduct():
        #Bajar la cantidad de un producto que esta en el pedido

        #Si la cantidad llega a 0, eliminarlo del pedido
        pass
    
    @staticmethod
    def getCosto():
        pass

    @staticmethod
    def getProductInOrder(order, id)->dict:
        for info in order:
            if info.get("id") == id:
                return info
        raise ValueError(f"No se logro encontrar el producto con id: {id} ,dentro del pedido")
    
    @staticmethod
    def getIndexProductInOrder(order:list, id:str)->int:
        for i, info in enumerate(order):
            if info.get("id") == id:
                return i
        raise ValueError(f"No se logro encontrar el producto con id: {id} ,dentro del pedido")

    @staticmethod
    def formatProductInfo(infoProduct:dict)->dict: #Aqui enviamos los datos que nos interesan del producto para tener en nuestro pedido
        return {"id": infoProduct.get("id"), "name": infoProduct.get("name"), "price": infoProduct.get("price"), "count" : 1}
        