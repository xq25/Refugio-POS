from service.service import Service
from helpers import utils

class TableService(Service):

    def getAll(specificData):
        pass
    def getId(id):
        pass
    def add(jsonData):
        pass
    def delete(id):
        pass
    def update(id, newJsonData):
        pass
    def assingId()->str:
        data = utils.getDataBase("./Data/tables.json")
        size = len(data.get("tables"))
        return str(size + 1)


    