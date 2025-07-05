class ServiceOrder():
    #Esta clase representa los servicios especificos que requiere un pedido
    def getId(id:str)->dict:
        '''Esta funcion nos permite devolver el pedido que tenemos dentro de nuestra base de datos para trabajar con el'''
        pass
    
    def addProduct(idProduct:str):
        '''Esta funcion nos permiteagregar un nuevo producto a nuestro pedido actual.
        Esto lo hacemos mediante el id del producto seleccionado en una lista desplegable
        '''
        pass
        
    def deleteProduct(id:str):
        '''Esta funcion nos permite eliminar un producto dentro de nuestro pedido.
        
        Posteriormente sera implementada en la clase de servicio del los pedidos'''
        pass

    def addUnitProduct():

        pass

    def deleteUnitProduct():
        #Bajar la cantidad de un producto que esta en el pedido

        #Si la cantidad llega a 0, eliminarlo del pedido
        pass

    def getCosto():
        '''Esta funcion permite calcular el costo teniendo en cuenta distintos factores, como promociones, dias de la semana, etc'''
        
        pass