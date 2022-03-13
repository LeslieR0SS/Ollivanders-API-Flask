from flask_restful import Resource


class quality(Resource, quality=None):
    def get(self):
        if quality:
            return 'Hola, {0} tienes {1} años.'.format(quality)
        else:
            return {"hello": "qualityyyyyy"}