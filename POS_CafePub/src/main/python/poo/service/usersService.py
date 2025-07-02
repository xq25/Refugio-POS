from helpers import utils
from service.service import Service
import bcrypt

# --- Nota ---‼️
#   CurrentUser es un diccionario sobre el cual tenemos acceso despues de loggearnos de manera adecuada y correcta con un usuario
#--------------------------------------------------------------------------------------------------------------------------------

class UserService(Service):
    # --- Herencia de Service --- ⚙️
    @staticmethod
    def getId(user_id)->dict:
        data = utils.getDataBaseUsers()  #Base de datos general
        admins_ids = UserService.getAdminListId()  #lista de ids de los admins
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
    
    @staticmethod
    def add(userJson:dict):
        dataBase = utils.getDataBaseUsers()
        userRank = userJson.get("rank")

        key = UserService.clasificator(userRank)
        specificData = dataBase.get({f"{key}"})
        specificData.append(userJson)
        dataBase[f"{key}"] = specificData

        utils.safetysave("./Data/users.json", dataBase)

    @staticmethod
    def delete(userId, currentUser):

        delete_user = UserService.getId(userId)
        if UserService.hierarchiesValidation(currentUser):
            userRank = delete_user.get("rank")
            if UserService.rankValidation(userRank):
                if userRank == 2:
                    raise ValueError("No se puede eliminar este usuario")
                else:
                    deleteIndex = UserService.getIndexUserId(userId,userRank)
                    dataBase = utils.getDataBaseUsers()
                    key = UserService.clasificator(userRank)

                    deleteList = dataBase.get(key)
                    deleteList.pop(deleteIndex)

                    dataBase[key] = deleteList
                    utils.safetysave("./Data/users.json",dataBase)
            else:
                raise ValueError("El rango del usuario a eliminar esta por fuera de los parametros")
    
    @staticmethod
    def update(userId:str, newJsonData:dict, currentUser:dict):

        currentInfo = UserService.getId(userId)
        currentRank = currentInfo.get("rank")
        
        if UserService.accessInfoValidation(userId, currentUser):
            data = utils.getDataBaseUsers()

            if UserService.changeRankValidation(currentRank, newJsonData.get("rank")):
                UserService.delete(userId, currentUser)
                UserService.add(newJsonData)
            else:
                indexUpdate = UserService.getIndexUserId(userId)
                key = UserService.clasificator(currentRank)
                specificData = data.get(f"{key}")
                specificData[indexUpdate] = newJsonData

                data[f"{key}"] = specificData
                utils.safetysave("./Data/users.json", data)
                
    @staticmethod
    def assingId():
        count = UserService.numberOfUsers() + 1
        id = utils.orderId(str(count)) 

        return id
  
    # --- Validaciones --- ✅❌
    
    @staticmethod
    def nameValidation(userName)->bool:
        specialChars = "!@#$%^&*()_+-=[]/,.{}"
        if len(userName) < 3:
            raise ValueError("El nombre del usuario debe tener al menos 3 caracteres")
        for i in specialChars:
            if i in userName:
                raise ValueError("El nombre del usuario no puede contener caracteres especiales")
        return True
    @staticmethod
    def rankValidation(rank)->bool:
        if 0 <= rank < 2:
            return True
        else:
            raise ValueError("El rango ingresado es incorrecto, debe estar entre 0 y 1")

    @staticmethod
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

    @staticmethod   
    def hierarchiesValidation(currentUser)->bool:
        currentUserRank = currentUser.get("rank")
        if currentUserRank!= 1 and currentUserRank != 2:
            raise ValueError(f"El usuario {currentUser.get("id")} no tiene acceso!")
        else:   
            return True 

    @staticmethod
    def accessInfoValidation(idAcces:str, currentUser:dict)->bool:
        #idAcces es el id de la instancia sobre la cual queremos acceder o modificar
        if UserService.hierarchiesValidation(currentUser) or currentUser.get("id")== idAcces:
            return True
        else:
            raise PermissionError("No cuentas con los privilegios para acceder a esta informacion")

    @staticmethod 
    def changeRankValidation(currentRank, newRank):
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
            response = True
            print(" --- Acceso concedido --- ")
            print(f" --- Bienvenido Usuario {userInfo.get("name")} --- ")
            return response
        else:
            raise ValueError("La contraseña ingresada es incorrecta!")

    # --- Herramientas Utiles ---  
    @staticmethod  
    def getAdminListId()->list:
        idList = []
        dataBase = utils.getDataBaseUsers()
        adminList = dataBase.get("4dm1n")
        for a in adminList:
            idList.append(a.get("id"))
        
        return idList
    
    @staticmethod
    def getIndexUserId(user_id:str, rank:int)->int:#Terminar!!
        data = utils.getDataBaseUsers()
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
        data = utils.getDataBaseUsers()
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

    
