from flask import (
    Flask,
    redirect,
)  # importamos el mini framework de FLask y redirect (para redireccionar rutas)
from repository.db_uri import DB, HOST
from repository.connection import init_app
from services.services import atlas as db
import json


# Creación de la app Flask
app = Flask(__name__)
init_app(app, DB, HOST)

"""Las rutas de la API Rest"""

# GET -> es un tipo de petición. Sirve para obtener info.


@app.route("/", methods=["GET"])
def wellcome():
    return {"hello": "Ollivanders"}


@app.route("/items", methods=["GET"])
def get_items():
    # return "hola estos son los items"
    return db.get_items(DB, HOST)


@app.route("/items/<string:name>", methods=["GET"])
def item_by_name(name):
    return db.get_items_by_name(DB, HOST, name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8080)
    # el HOST es 0.0.0.0 para que desde cualquier ordenador se pueda abrir el programa desde su propio localhost
    # DEBUG -> para que se vaya actualizando el link mietras hagamos cambios
    # PORT-> sirve para especificar el puerto que deseamos abrir. Según el quickstart de flask es 8080.
