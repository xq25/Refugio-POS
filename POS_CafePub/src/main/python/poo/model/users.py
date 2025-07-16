import json
from helpers import utils

class Users():
    def __init__(self,id, name:str, password:str, rank:int):
        self.__id = id
        self.__name = name.capitalize()
        try:
            if Users.rankValidation(rank):
                self.__rank = rank
                if rank == 0:
                    self.__password = ""
                else:
                    if Users.passwordValidation(password):
                        self.__password = utils.encryptString(password).decode()
        except ValueError as error :
            raise error

    @staticmethod
    def fromJson(jsonData:dict):#fundamental!!, la informacion del usuario debe ser ingresada en texto plano desde el frontEnd para ser encryptada por el backend
        info = json.loads(jsonData) 
        Users(info.get("id"),info.get("name"),info.get("password"),info.get("rank"))

    def toDict(self):
        return {"id": self.__id,
                "name": self.__name, 
                "password": self.__password, 
                "rank":self.__rank
                }

    #Accesores y Mutadores
    def getId(self):
        return self.__id
    #El id del usuario no es modificable. despues de la primera asignacion ese sera siempre su id
    def getName(self):
        return self.__name
    def setName(self, newName:str):
        if Users.nameValidation(newName):
            self.__name = newName

    def getRank(self):
        return self.__rank 
    def setRank(self, newRank:int):
        try:
            if  Users.rankValidation(newRank):
                self.__rank = newRank
        except ValueError as error:
            raise error
    
    def getPassword(self):
        return self.__password    
    def setPassword(self, newPassword:str):
        if self.__rank == 0 :  
            raise ValueError("Los empleados no requieren contraseña")
        else: 
            #Solo los administradores y diseñadores pueden tener contraseña
            if Users.passwordValidation(newPassword):
                self.__password = utils.encryptString(newPassword)
                    
    @staticmethod
    def nameValidation(userName:str)->bool:
        
        if len(userName) < 3 and len(userName) > 20:
            raise ValueError("El nombre del usuario debe ser de 3 a 20 caracteres")
        if utils.stringValidation(userName):
            return True
    
    @staticmethod
    def rankValidation(rank:int)->bool:
        #Excepciones
        if not isinstance(rank, int):
            raise ValueError("El dato ingresado para el rango debe ser un valor numerico entero")
        if rank < 0 or rank >1:
            raise ValueError("El rango ingresado es incorrecto, debe estar entre 0 y 1")
        
        return True

    @staticmethod
    def passwordValidation(password):
        numValidation = False
        if len(password) < 6 :
            raise ValueError("La contraseña debe tener al menos 6 caracteres")
        for i in range(10):
            if str(i) in  password:
                numValidation = True
        if numValidation == False:
            raise ValueError("La contraseña debe tener al menos un numero entero")
        return True
