from Model.src.Helpers import utils
import json
import bcrypt

# --- Nota ---‼️
#CurrentUser es un diccionario sobre el cual tenemos acceso despues de loggearnos de manera adecuada y correcta con un usuario

def getAdminListId()->list:
    idList = []
    dataBase = utils.getDataBaseUsers()
    adminList = dataBase.get("4dm1n")
    for a in adminList:
        idList.append(a.get("id"))
    
    return idList

def getUserId(user_id)->dict:
    data = utils.getDataBaseUsers()  #Base de datos general
    admins_ids = getAdminListId()  #lista de ids de los admins
    developer = data.get("d3v3l0p3r") #diccionario con la informacion del ingeniero
    only_admins = data.get("4dm1n", []) #Lista de diccionarios con informacion de los administradores 
    only_employees = data.get("general", []) # lista de diccionarios con la informacion de todods los empleados

    # Buscar desarrollador (tiene prioridad si coincide el id)
    if developer and developer.get("id") == user_id:
        return developer

    # Buscar entre admins
    elif user_id in admins_ids:
        for admin in only_admins:
            if admin.get("id") == user_id:
                return admin

    else:
        # Buscar entre empleados
        for employee in only_employees:
            if employee.get("id") == user_id:
                return employee

    # Si no se encuentra el usuario
    raise ValueError(f"No se encontró el usuario con el ID: {user_id}")

def getNumUserId(user_id)->int:
    data = utils.getDataBaseUsers()
    admins_ids = getAdminListId()  #lista de ids de los admins
    developer = data.get("d3v3l0p3r") #diccionario con la informacion del ingeniero
    only_admins = data.get("4dm1n", []) #Lista de diccionarios con informacion de los administradores 
    only_employees = data.get("general", []) # lista de diccionarios con la informacion de todods los empleados

    # Buscar desarrollador (tiene prioridad si coincide el id)
    if developer and developer.get("id") == user_id:
        return 0

    # Buscar entre admins
    if user_id in admins_ids:
        for i , admin in enumerate(only_admins):
            if admin.get("id") == user_id:
                return i
    else:
        # Buscar entre empleados
        for i , employee in enumerate(only_employees):
            if employee.get("id") == user_id:
                return i

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
        raise ValueError("Algo salio terriblemente mal en las validaciones de los rangos ")

    utils.safetysave("./Data/users.json",dataBase)

def deleteUser(userId, currentUser):

    delete_user = getUserId(userId)
    if hierarchiesValidation(currentUser):
        userRank = delete_user.getRank()
        if rankValidation(userRank):
            if userRank == 2:
                raise ValueError("No se puede eliminar este usuario")
            else:
                deleteIndex = getNumUserId(userId)
                dataBase = utils.getDataBaseUsers()
                if  userRank == 1:
                    key = "4dm1n"
                elif userRank == 0:
                    key = "general"

                deleteList = dataBase.get(key)
                deleteList.pop(deleteIndex)

                dataBase[key] = deleteList
                utils.safetysave("./Data/users.json",dataBase)
        else:
            raise ValueError("El rango del usuario a eliminar esta por fuera de los parametros")

def nameValidation(userName)->bool:
    specialChars = "!@#$%^&*()_+-=[]/,.{}"
    if len(userName) < 3:
        raise ValueError("El nombre del usuario debe tener al menos 3 caracteres")
    for i in specialChars:
        if i in userName:
            raise ValueError("El nombre del usuario no puede contener caracteres especiales")
    return True

def rankValidation(rank)->bool:
    if 0 <= rank < 2:
        return True
    else:
        raise ValueError("El rango ingresado es incorrecto, debe estar entre 0 y 1")

def newPasswordValidation(currentPassword,newPassword)->bool:
    numValidation = False
    if len(newPassword) < 6 :
        raise ValueError("La contraseña debe tener al menos 6 caracteres")
    for i in range(10):
        if str(i) in  newPassword:
            numValidation = True
    if numValidation == False:
        raise ValueError("La contraseña debe tener al menos un numero")
    if newPassword == currentPassword:
        raise ValueError("Debes ingresar una contraseña diferente a la que ya tienes")
    return True
    
def hierarchiesValidation(currentUser)->bool:
    currentUserRank = currentUser.get("rank")
    if currentUserRank!= 1 and currentUserRank != 2:
        raise ValueError(f"El usuario {currentUser.get("id")} no tiene acceso!")
    else:   
        return True 

def accessInfoValidation(idAcces, currentUser)->bool:
    if hierarchiesValidation(currentUser) or currentUser.get("id")== idAcces:
        return True
    else:
        raise PermissionError("No cuentas con los privilegios para acceder a esta informacion")

def numberUsers()->int:
    data = utils.getDataBaseUsers()
    count = 0
    for key in data.keys():
        if isinstance(data[f"{key}"],dict):
            count +=1
        else: 
            count += len(data[f"{key}"])
    return count

def loginverify(userID:str, passwordUser)->bool:#Validacion de contrasena perteneciente al usuario
    userInfo = getUserId(str(userID))
    hashSave = userInfo.get("password").encode() #encode convierte nuestro string en una cadena de bits
    
    if bcrypt.checkpw(passwordUser.encode(), hashSave):  #Validamos que la contra ingresada por el usuario al momento de ser codificada nos da una igualdad o similitud con el hash que teniamos en la base de datos
        response = True
        print(" --- Acceso concedido --- ")
        print(f" --- Bienvenido Usuario {userInfo.get("name")} --- ")
        return response
    else:
        raise ValueError("La contraseña ingresada es incorrecta!")
        




#Todas las funcionalidades de los usuarios dependen del usuario sobre el cual estamso accediendo a la info, dependiendo de su rango puede realizar mas o menos operaciones

    
