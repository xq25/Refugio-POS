from abc import ABC, abstractmethod

class Service(ABC):
    
    @abstractmethod
    def getAll(specificData:list)->list:
        '''Esta funcion nos permite obtener todos las instancias de un tipo especifico, siendo asi adaptable para usuarios
        y productos.
        
        Posteriormente sera implementada en las clases de servicios'''
        pass

    def getId(id:str)->dict:
        '''Esta funcion permite tener acceso a la informacion puntual de una instancia guardada
        dentro de nuestra base de datos, siempre y cuando tenga una clave "id"

        Posteriormente se tomara en cuenta dentro de las respectivas clases que heredan de service
        aplicandolo cada una de una forma distinta con sus respectivas validaciones.
        '''
        pass
    @abstractmethod
    def add(jsonData:dict)->None:
        '''Esta funcion recibe la informacion en un formato diccionario o json 
        para asi ser enviada a su respectiva clasificacion dentro de nuestra base de datos.

        Posteriormente se tomara en cuenta dentro de las respectivas clases que heredan de service
        aplicandolo cada una de una forma distinta con sus respectivas validaciones.
        '''
        pass
    def delete(id:str):
        '''Esta funcion recibe el id de la instancia almacenada en nuestra base de datos que desea ser eliminada
        primero validando que la id ingresada exista dentro de nuestra base de datos.

        Posteriormente esta funcion sera implementada en base a ciertas restricciones de cada clase de servicio.
        '''
        pass
    
    def update(id:str, newJsonData:dict):
        '''Esta funcion recibe el id de la instancia que vamos a modificar y a su vez tambien la informacion modificada
        de esta misma instancia, para asi ser remplazada dentro de nuestra base de datos.
        
        Posteriormente esta funcion sera implementada en base a las restricciones de cada clase de servicio.
        '''
        pass
    
    def assingId():
        '''Todas las clases de servicios deben contar con un metodo que permita individualizar las instancias de las clases 
        a las cuales pertenece'''
        pass
    
    #def getIdex(index:int)->dict:
    #     '''Esta funcion nos permite acceder a la informacion dentron de nuestra base de datos mediante un indice.
    #     Esto es debido a que guardamos nuestros elementos en listas dentro de nuestra base de datos clasificada.

    #     Posteriormente se tomara en cuenta dentro de las respectivas clases que heredan de service
    #     aplicandolo cada una de una forma distinta con sus respectivas validaciones.
    #     '''
    #     pass