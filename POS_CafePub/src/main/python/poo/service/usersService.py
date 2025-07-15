from helpers import utils
from service.service import Service
import bcrypt
from model.users import Users

# --- Nota ---‼️
#   CurrentUser es un diccionario con toda la informacion de un usuario. Sobre el cual tenemos acceso despues de loggearnos de manera adecuada y correcta con un usuario
#--------------------------------------------------------------------------------------------------------------------------------

class UserService(Service):
    # --- Herencia de Service --- ⚙️

    @staticmethod
    def getAll()->dict:
        dataBase = utils.getDataBase("./Data/users.json")
        data = dataBase.get("4dm1n") + dataBase.get("general")

        return {"status": "success","message" : "Se cargo de manera exitosa la base de datos!", "data" : data}
        
    @staticmethod
    def getId(user_id)->dict:
        data = utils.getDataBase("./Data/users.json")  #Base de datos general
        admins_ids = UserService.getAdminListId()  #lista de ids de los admins
        developer = data.get("d3v3l0p3r") #diccionario con la informacion del ingeniero
        only_admins = data.get("4dm1n", []) #Lista de diccionarios con informacion de los administradores 
        only_employees = data.get("general", []) # lista de diccionarios con la informacion de todods los empleados

        info = None
        # Buscar desarrollador (tiene prioridad si coincide el id)
        if developer and developer.get("id") == user_id:
            info = developer

        # Buscar entre admins
        elif user_id in admins_ids:
            for admin in only_admins:
                if admin.get("id") == user_id:
                    info = admin
        else:
            # Buscar entre empleados
            for employee in only_employees:
                if employee.get("id") == user_id:
                    info =  employee

        if info is not None:
            return info
        else:# Si no se encuentra el usuario
            raise ValueError(f"No se encontró el usuario con el ID: {user_id}")
    
    @staticmethod
    #Todos nuestros metodos devuelven un diccionario aclarando si el procedimiento se pudo aplicar con exito
    def add(userJson:dict)->dict:
        try:
            if not "id" in userJson:
                userJson["id"] = UserService.assingId()

            user = Users.fromJson(userJson).toJson()
            
            dataBase = utils.getDataBase("./Data/users.json")
            userRank = user.get("rank")

            key = UserService.clasificator(userRank)

            specificData = dataBase.get(f"{key}")
            specificData.append(user)
            dataBase[f"{key}"] = specificData

            utils.safetysave("./Data/users.json", dataBase)
            return {"message": "Usuario agregado con exito!", "data": user}
        except ValueError as e:
            raise e

    @staticmethod
    def delete(userId, currentUser)->dict:

        delete_user = UserService.getId(userId)
        if UserService.hierarchiesValidation(currentUser):
            userRank = delete_user.get("rank")
            if UserService.rankValidation(userRank):
                if userRank == 2:
                    raise ValueError("No se puede eliminar este usuario")
                else:
                    deleteIndex = UserService.getIndexUserId(userId,userRank)
                    dataBase = utils.getDataBase("./Data/users.json")
                    key = UserService.clasificator(userRank)

                    deleteList = dataBase.get(key)
                    deleteList.pop(deleteIndex)

                    dataBase[key] = deleteList
                    utils.safetysave("./Data/users.json",dataBase)
                    return {"status": "success", "message": f"Usuario {userId} Eliminado con Exito!", "data": delete_user}
            else:
                raise ValueError("El rango del usuario a eliminar esta por fuera de los parametros")

    @staticmethod
    def update(userId:str, newJsonData:dict, currentUser:dict)->dict:

        currentInfo = UserService.getId(userId)
        currentRank = currentInfo.get("rank")
        
        if UserService.accessInfoValidation(userId, currentUser):
            data = utils.getDataBase("./Data/users.json")

            if UserService.changeRankValidation(currentRank, newJsonData.get("rank")):

                if userId == "JQ001":
                    raise ValueError("El desarrollador no puede modificar su rango por motivos de seguridad")
                else:
                    UserService.delete(userId, currentUser)  
                    #Si el add presenta alguna falla debemos reestablecer los cambios
                    UserService.add(newJsonData)
            else:
                indexUpdate = UserService.getIndexUserId(userId)
                key = UserService.clasificator(currentRank)
                specificData = data.get(f"{key}")
                specificData[indexUpdate] = newJsonData

                data[f"{key}"] = specificData
                utils.safetysave("./Data/users.json", data)
                return {"status": "success", "message": f"El usuario {userId} fue actualizado con exito!", "data":  newJsonData}
                
    @staticmethod
    def assingId()->str:
        count = UserService.numberOfUsers() + 1
        id = utils.orderId(str(count)) 

        return id
  
    # --- Validaciones --- ✅❌
    @staticmethod
    def newPasswordValidation(currentPassword,newPassword)->bool:
        
        if newPassword == currentPassword:
            raise ValueError("Debes ingresar una contraseña diferente a la que ya tienes")
        try:
            UserService.passwordValidation(newPassword)
            return True
        except ValueError as e:
            raise e
            
    @staticmethod   
    def hierarchiesValidation(currentUser)->bool:
        '''Esta funcion nos permite validar si el usuario tiene el rango o privilegios requeridos
        para realizar cambios sobre los productos.'''

        currentUserRank = currentUser.get("rank")
        if currentUserRank!= 1 and currentUserRank != 2:
            raise ValueError(f"El usuario {currentUser.get("id")} no tiene acceso!")
        else:   
            return True 

    @staticmethod
    def accessInfoValidation(idAcces:str, currentUser:dict)->bool:
        '''Esta funcion nos permite saber si el usuario actual tiene acceso sobre
        la informacion especifica de un usuario'''

        #idAcces es el id de la instancia sobre la cual queremos acceder o modificar
        if UserService.hierarchiesValidation(currentUser) or currentUser.get("id")== idAcces:
            return True
        else:
            raise PermissionError("No cuentas con los privilegios para acceder a esta informacion")

    @staticmethod 
    def changeRankValidation(currentRank:int, newRank:int):
        '''Esta funcion es util para com parar si un rango cambio durante un proceso de actualizacion(update)
        para asi realizar otras validaciones'''

        if newRank != currentRank:
            return True
        else:
            return False
    # --- Validacion de acceso e inicio de sesion ---
    @staticmethod
    def loginverify(userID:str, passwordUser)->bool:#Validacion de contrasena perteneciente al usuario
        userInfo = UserService.getId(str(userID))
        hashSave = userInfo.get("password").encode() #encode convierte nuestro string en una cadena de bits
        
        if bcrypt.checkpw(passwordUser.encode(), hashSave):  #Validamos que la contra ingresada por el usuario al momento de ser codificada nos da una igualdad o similitud con el hash que teniamos en la base de datos
            print(" --- Acceso concedido --- ")
            print(f" --- Bienvenido Usuario {userInfo.get("name")} --- ")
            return True
        else:
            raise ValueError("La contraseña ingresada es incorrecta!")

    # --- Herramientas Utiles ---  
    @staticmethod  
    def getAdminListId()->list:
        idList = []
        dataBase = utils.getDataBase("./Data/users.json")
        adminList = dataBase.get("4dm1n")
        for a in adminList:
            idList.append(a.get("id"))
        
        return idList
    
    @staticmethod
    def getIndexUserId(user_id:str, rank:int)->int:
        data = utils.getDataBase("./Data/users.json")
        rank_Key = ""
        userInfo = UserService.getId(user_id)

        if userInfo:#Verificacion de que el id ingresado si pertenezca a un usuario en nuestra base de datos
            
            if rank == 2: #El usuario desarrollador no se puede eliminar
                raise ValueError(f"Los desarrolladores no requieren un indice que los identifique")
            else:
                #Asignacion de key para ingresar a la base de datos especifica de cada jerarquia
                if rank == 1: 
                    rank_Key = "4dm1n"
                else:
                    rank_Key = "general"
                
                specificData = data.get(rank_Key)
                index = None

                for i,info in enumerate(specificData):
                    if info.get("id") == user_id:
                        index = i
                if index is not None: #Validamos que exista un indice(Siempre deberia de existir ya que el usuario existe)
                    return index
                else:
                    raise ValueError(f"Algo salio mal en el proceso de buscar el indice del usuario con id: {user_id}")

        else:
            # Si no se encuentra el usuario
            raise ValueError(f"No se encontró el usuario con el ID: {user_id}") 
        
    @staticmethod
    def numberOfUsers()->int:
        data = utils.getDataBase("./Data/users.json")
        count = 0
        for key in data.keys():
            if isinstance(data[f"{key}"],dict):
                count +=1
            else: 
                count += len(data[f"{key}"])
        return count
    
    @staticmethod
    def clasificator(rank:int)->str:
        key = ""
        if rank == 1:
            key = "4dm1n"
        elif rank == 0:
            key = "general"
        else:
            raise ValueError(f"El rango ingresado no esta dentro de la informacion visible al publico de la base de datos")
        
        return key
    
#Todas las funcionalidades de los usuarios dependen del usuario sobre el cual estamso accediendo a la info, dependiendo de su rango puede realizar mas o menos operaciones

    
