from flask_restful import Resource
from repository.db_mocked import DB


class item(Resource):
    def get(self):
        return 'los items individuales'