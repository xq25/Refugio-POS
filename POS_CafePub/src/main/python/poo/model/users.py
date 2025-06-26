import json
from service import usersService as Usrs
from helpers import utils

class Users():
    def __init__(self, name:str, password:str, rank:int, id = str(Usrs.numberUsers() + 1)):
        self.__id = id
        self.__name = name.capitalize()
        try:
            if Usrs.rankValidation(rank):
                self.__rank = rank
                if rank == 0:
                    self.__password = ""
                else:
                    if Usrs.newPasswordValidation("",password):
                        self.__password = utils.encryptString(password).decode()
        except ValueError as error :
            print(f"Error: {error}")

    def fromJson(jsonData):#fundamental!!, la informacion del usuario debe ser ingresada en texto plano desde el frontEnd para ser encryptada por el backend
        info = json.loads(jsonData) 
        Users(info.get("name"),info.get("password"),info.get("rank"))

    def toJson(self):
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
        self.__name = newName

    def getRank(self):
        return self.__rank 
    def setRank(self, newRank:int, currentUser):
        try:
            if Usrs.hierarchiesValidation(currentUser): 
                print(" --- Full Access!! --- ")
                if  Usrs.rankValidation(newRank):
                    self.__rank = newRank
        except ValueError as error:
            print(f"Error: {error}")
    
    def getPassword(self, currentUser):
        try:
            if Usrs.accessInfoValidation(self.getId(), currentUser):
                return self.__password
        except PermissionError as error:
            print(f"Error : {error}")
        
    def setPassword(self, newPassword:str):
        if self.__rank == 0 :  
            print("Los empelados no requieren una contraseña")
        else: #Solo los administradores y diseñadores pueden tener contraseña
            try:
                if Usrs.newPasswordValidation(self.__password, newPassword): #Si la contraseña cumple con los estandares se aplica el cambio
                    self.__password = utils.encryptString(newPassword)
            except ValueError as error:
                print(f"Error : {error}")
                