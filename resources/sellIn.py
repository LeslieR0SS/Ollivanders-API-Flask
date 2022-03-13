from flask_restful import Resource


class sellIn(Resource):
    def get(self):
        return {"hello": "SEllll IN"}