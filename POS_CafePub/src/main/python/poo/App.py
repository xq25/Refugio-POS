from model.drinks import Drinks
from service.productsService import ProductService
from model.drinkBases import DrinksBases
from helpers import utils

d = Drinks("CKR27","Limonada Natural",7500, "", False, [DrinksBases.LIMON.value, DrinksBases.AGUA.value], {"hola": "si"} )
jsonData = utils.toJSONObject(d.toDict())
ProductService.add(jsonData)

