import json
import bcrypt
import os
import string
import random

ROJO = "\033[31m"
RESET = "\033[0m"

def getDataBase(path:str)->dict:
    try:
        with open(path,"r") as file:
            info = json.load(file)
        return info
    except FileNotFoundError:
        raise (f"No se Encontro el Archivo: \033[3m{path}033[0m")

def orderId(num:str)->int: #Esta funcion es ajustable a la cantidad de productos maxima en nuestra base de datos 
    lenght = len(num)
    id = ("0"*(3-lenght))+num #(el 3 referencia que puede asignar id hasta 999 productos por cada tipo)
    return id

def encryptString(string:str)->str:
    hashed = bcrypt.hashpw(string.encode(), bcrypt.gensalt())
    return hashed

def safetysave(path, data)->None: #Esta funcion genera un archivo temporal con los datos editados de nuestra base de datos para asi remplazar el original al momento de comprobar que todo haya salido bien

    tempPath = path + ".temp"
    try:
        with open(tempPath, "w") as temp_File:
            json.dump(data, temp_File, indent=4)

        os.replace(tempPath, path)#remplazamos el archivo original por el temporal, si no hay errores
        

    except Exception as error:
        if os.path.exists(tempPath): #Si en algun momento se llego a generar el archivo pero aun asi salio algo mal, se elimina
            os.remove(tempPath)
        raise error  #Mostramos que fallo

def stringValidation(string)->bool:
    specialChars = "!@#$%^&*()_+-=[]/,.{}"

    for i in specialChars:
        if i in string:
            raise ValueError(f"La cadena no puede contener caracteres especiales como : {i}")
    return True 

def randomString(length:int) ->str:
    caracteres = string.ascii_uppercase  # Solo A-Z
    resultado = ''.join(random.choice(caracteres) for _ in range(length))
    return resultado

def showTraceError(exception : Exception):
    print(f"{ROJO} ------- REPORTE DE EXCEPCIONES ------- {RESET}")
    print(exception)
    print(f"{ROJO} ------- FIN DEL REPORTE DE EXCEPCIONES -------{RESET}")