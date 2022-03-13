from distutils.log import debug
from flask import Flask 
from flask_restful import Api


from resources.home import home
from resources.stock import stock
from resources.item import item
from resources.quality import quality
from resources.sellIn import sellIn
# from flask import url_for

def create_app():
    #iniciador de flask
    app = Flask(__name__)
    
    #Para poder testear la API rest
    api = Api(app, catch_all_404s=True)
    
    
    api.add_resource(home, "/")
    api.add_resource(stock, '/stock')
    # api.add_resource(item, '/items/<name>')
    # api.add_resource(quality, '/items/quality/<int:quality>')
    # api.add_resource(sellIn, '/items/sell_in/<int:sell_in>')

    
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
    app.run(host="0.0.0.0", debug=True, port=8080)
