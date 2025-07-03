from service.usersService import UserService
from model.users import Users

# u = Users("Jacobo Quintero", "123", 0)
# UserService.add(u.toJson())
UserService.update("003", {
            "id": "003",
            "name": "Jacobo Quintero",
            "password": "",
            "rank": 1
        },{
        "id": "JQ001",
        "name": "Jacobo Quintero",
        "password": "$2b$12$YLH0Qgjj9TViowouOuMzd.qgEPIufoXzXqj5cOZYKNnnSCHALuz9y",
        "rank": 2
    })