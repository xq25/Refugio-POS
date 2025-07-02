from model.beers import Beers
from service.productsService import ProductService

ProductService.delete("BR002", {
        "id": "001",
        "name": "Jacobo Quintero",
        "password": "$2b$12$YLH0Qgjj9TViowouOuMzd.qgEPIufoXzXqj5cOZYKNnnSCHALuz9y",
        "rank": 2
    },)