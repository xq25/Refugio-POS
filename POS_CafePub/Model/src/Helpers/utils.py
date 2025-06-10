import json
import bcrypt


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
        raise ("No se Encontro el Archivo: \033[3m./Data/products.json\033[0m")

def orderId(num:str): #Esta funcion es ajustable a la cantidad de productos maxima en nuestra base de datos 
    lenght = len(num)
    id = ("0"*(3-lenght))+num #(el 3 referencia que puede asignar id hasta 999 productos por cada tipo)
    return id

def encryptString(string):
    pass
