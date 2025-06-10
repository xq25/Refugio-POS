from Model.src.Helpers import utils
import json

def getAdminsId():
    dataBase = utils.getDataBaseUsers()
    adminList = dataBase["4dm1n"].get("id")
    return adminList

def getUserId(user_id):
    data = utils.getDataBaseUsers()  #Base de datos general
    admins_ids = getAdminsId()  #lista de ids de los admins
    developer = data.get("d3v3l0p3r") #diccionario con la informacion del ingeniero
    only_admins = data.get("4dm1n", []) #Lista de diccionarios con informacion de los administradores 
    only_employees = data.get("general", []) # lista de diccionarios con la informacion de todods los empleados

    # Buscar desarrollador (tiene prioridad si coincide el id)
    if developer and developer.get("id") == user_id:
        return developer

    # Buscar entre admins
    if user_id in admins_ids:
        for admin in only_admins:
            if admin.get("id") == user_id:
                return admin

    # Buscar entre empleados
    for employee in only_employees:
        if employee.get("id") == user_id:
            return employee

    # Si no se encuentra el usuario
    raise ValueError(f"No se encontró el usuario con el ID: {user_id}")

def addUser(userJson):
    dataBase = utils.getDataBaseUsers()
    userRank = userJson.get("rank")

    if userRank == 1: 
        admins = dataBase.get("4dm1n")
        admins.append(userJson)
        dataBase["4dm1n"] = admins
    elif userRank == 0:
        employees = dataBase.get("general")
        employees.append(userJson)
        dataBase["general"] = employees
    else:
        print("Algo salio terriblemente mal en las validaciones de los rangos ")

    with open("./Data/users.json", "W")as update:
        json.dump(dataBase, update, indent=4)

def deleteUser(idUser):
    pass

def deleteValidations(idUser, currentUser): #Verificar que otras validaciones hayq eu tener en cuenta antes de eliminar un usuario
    if hierarchiesValidation(currentUser):
        pass

     #No se puede eliminar un administrador si el usuario es un empleado

def rankValidation(newRank):
    if 0 <= newRank < 2:
        return True
    else:
        return False

def verifyPassword(idUser,password): #Verificacion de coincidencia entre id y contrasena del usuario
    user = getUserId(idUser)
    if user.getPassword(user) == password:
        print(" --- Acceso concedido --- ")
        print(f" --- Bienvenido Usuario {user.getName()} --- ")
        return True
    else:
        return False

def newPasswordValidation(currentPassword,newPassword):
    numValidation = False
    if len(newPassword) < 6 :
        raise ValueError("La contraseña debe tener al menos 6 caracteres")
    for i in range(newPassword):
        if str(i) in  newPassword:
            numValidation = True
    if numValidation == False:
        raise ValueError("La contraseña debe tener al menos un numero")
    if newPassword == currentPassword:
        raise ValueError("Debes ingresar una contraseña diferente a la que ya tienes")
    return True
    
def hierarchiesValidation(currentUser):
    if currentUser.getRank() != 1 and currentUser.getRank() != 2:
        return False
    else:   
        return True 

def accessInfoValidation(idAcces, currentUser):
    if hierarchiesValidation(currentUser) or currentUser.getId() == idAcces:
        return True
    else:
        return False



#Todas las funcionalidades de los usuarios dependen del usuario sobre el cual estamso accediendo a la info, dependiendo de su rango puede realizar mas o menos operaciones

    
