from pymongo import MongoClient

# Responsável por acessar o banco de dados
class CambioRepository:
    def __init__(self, mongo_uri, mongo_db):
        self.client = MongoClient(mongo_uri)
        self.collection = self.client[mongo_db]["db_cambio"]
        
    def insert(self, db_cambio):
        # Insere um documento moeda na coleção
        self.collection.insert_one(db_cambio.to_dict())
        