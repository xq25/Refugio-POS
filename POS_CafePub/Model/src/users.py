import json
from Model.src.Service import usersService as Usrs

class Users():
    def __init__(self,id, name, password = "", rank = 0):
        self.__id = id
        self.__name = name
        self.__rank = rank
        self.__password = password


    #Accesores y Mutadores
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
    def setName(self, newName):
        self.__name = newName

    def getRank(self):
        return self.__rank 
    def setRank(self, newRank, currentUser):
        if Usrs.hierarchiesValidation(currentUser): 
            print(" --- Full Access!! --- ")
            if  Usrs.rankValidation(newRank):
                self.__rank = newRank
            else:
                raise ("Tienes que ingresar un rango entre 0 y 1")
        else:
            raise(f"User : {currentUser.getName()} hasn't access!")
    
    def getPassword(self, currentUser):
        if Usrs.accessInfoValidation(self.getId(), currentUser):
            return self.__password
        else: 
            raise PermissionError("No cuentas con los privilegios para acceder a esta informacion")
    def setPassword(self, newPassword):
        if self.__rank == 0 :  
            raise ValueError("Los empelados no requieren una contraseña")
        else: #Solo los administradores y diseñadores pueden tener contraseña
            if Usrs.newPasswordValidation(self.__password, newPassword): #Si la contraseña cumple con los estandares se aplica el cambio
                self.__password = newPassword
            