import json
from service.tableService import TableService

class Tables():
    def __init__(self, reference:str, order:list, tableId = TableService.assingId()):

        self.__tableId = tableId
        self.__reference = reference
        self.__order = order

    @staticmethod
    def fromJson(jsonData):
        info = json.loads(jsonData)

        Tables(info.get("reference"), info.get("order"))