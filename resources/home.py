from flask_restful import Resource


class home(Resource):
    def get(self):
        return {"hello": "Ollivanders"}