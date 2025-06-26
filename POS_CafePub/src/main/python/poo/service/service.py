from abc import ABC, abstractmethod

class Service(ABC):
    def getID(id:str)->dict:
        '''Esta funcion permite etener acceso a la informacion puntual de una instancia guardada
        dentro de nuestra base de datos, siempre y cuando tenga una clave "id"

        Posteriormente se tomara en cuenta dentro de las respectivas clases que heredan de service
        aplicandolo cada una de una forma distinta con sus respectivas validaciones.
        '''
        pass
    def getIdex(index:int)->dict:
        '''Esta funcion nos permite acceder a la informacion dentron de nuestra base de datos mediante un indice.
        Esto es debido a que guardamos nuestros elementos en listas dentro de nuestra base de datos clasificada.

        Posteriormente se tomara en cuenta dentro de las respectivas clases que heredan de service
        aplicandolo cada una de una forma distinta con sus respectivas validaciones.
        '''
        pass
    def add(jsonData:dict)->None:
        '''Esta funcion recibe la informacion en un formato diccionario o json 
        para asi ser enviada a su respectiva clasificacion dentro de nuestra base de datos.

        Posteriormente se tomara en cuenta dentro de las respectivas clases que heredan de service
        aplicandolo cada una de una forma distinta con sus respectivas validaciones.
        '''
        pass

