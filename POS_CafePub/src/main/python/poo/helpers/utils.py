import json
import bcrypt
import os


def getDataBaseProducts():
    try:
        with open("./Data/products.json","r") as file:
            info = json.load(file)
        return info
    except FileNotFoundError:
        raise ("No se Encontro el Archivo: \033[3m./Data/products.json\033[0m")

def getDataBaseUsers():
    try:
        with open("./Data/users.json","r") as file:
            info = json.load(file)
        return info
    except FileNotFoundError:
        raise ("No se Encontro el Archivo: \033[3m./Data/users.json\033[0m")

def orderId(num:str): #Esta funcion es ajustable a la cantidad de productos maxima en nuestra base de datos 
    lenght = len(num)
    id = ("0"*(3-lenght))+num #(el 3 referencia que puede asignar id hasta 999 productos por cada tipo)
    return id

def encryptString(string:str):
    hashed = bcrypt.hashpw(string.encode(), bcrypt.gensalt())
    return hashed

def safetysave(path, data): #Esta funcion genera un archivo temporal con los datos editados de nuestra base de datos para asi remplazar el original al momento de comprobar que todo haya salido bien
    tempPath = path + ".temp"
    try:
        with open(tempPath, "w") as temp_File:
            json.dump(data, temp_File, indent=4)

        os.replace(tempPath, path)#remplazamos el archivo original por el temporal, si no hay errores

    except Exception as error:
        if os.path.exists(tempPath): #Si en algun momento se llego a generar el archivo pero aun asi salio algo mal, se elimina
            os.remove(tempPath)
        raise error  #Mostramos que fallo