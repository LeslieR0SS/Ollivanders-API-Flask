from distutils.log import debug
from turtle import home
from flask import Flask 
from flask_restful import Api

# from flask import url_for

def create_app():
    #iniciador de flask
    app = Flask(__name__)
    api = Api(app, catch_all_404s=True)
    api.add_resource(home, "/")
    # api.add_resource(stock, '/stock')

    
    return app


# #Rutas estáticas
# @app.route('/') 
# def hello_world():
#     return '<h1>Hello World!</h1>'

# #Rutas dinánimas:

# @app.route("/hello/<string:nombre>")
# @app.route("/hello/<string:nombre>/<int:edad>")
# def hola(nombre=None,edad=None):
#     if nombre and edad:
#         return 'Hola, {0} tienes {1} años.'.format(nombre,edad)
#     elif nombre:
#         return 'Hola, {0}'.format(nombre)
#     else:
#         return 'Hola mundo'

if __name__ == '__main__':
    app = create_app()
    app.run()
