from distutils.log import debug
from flask import Flask 
# from flask import url_for
app = Flask(__name__)

#Rutas estáticas
@app.route('/') 
def hello_world():
    return '<h1>Hello World!</h1>'

#Rutas dinánimas:

@app.route("/hello/<string:nombre>")
@app.route("/hello/<string:nombre>/<int:edad>")
def hola(nombre=None,edad=None):
    if nombre and edad:
        return 'Hola, {0} tienes {1} años.'.format(nombre,edad)
    elif nombre:
        return 'Hola, {0}'.format(nombre)
    else:
        return 'Hola mundo'

if __name__ == '__main__':
    app.run('0.0.0.0',8080, debug= True)
