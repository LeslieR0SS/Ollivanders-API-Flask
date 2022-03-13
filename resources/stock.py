from flask_restful import Resource
from repository.db_mocked import DB


class stock(Resource):
    def get(self):
        return DB.inventario 