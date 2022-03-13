# **Proyecto: Flask API REST Ollivanders**

## **Descripción:**

En este proyecto vamos a desarrollar una [API REST](https://www.youtube.com/watch?v=HeXQ98sogs8&feature=youtu.be) con [Flask](https://flask.palletsprojects.com/en/1.1.x/) de la actividad de programación, llamada [Ollivanders Shop](https://github.com/dfleta/ollivanders_shop).

*Actividad propuesta por [@dfleta](https://github.com/dfleta/flask-rest-ci-boilerplate), profesor  de DAW dual - CIFP Borja Moll*

---

## **¿Qué es Flask?**

Flask es un "micro" framework escrito en Python y concebido para facilitar el desarrollo de aplicaciones Web bajo el patrón MVC, o incluso *Repository* en nuestro caso. Además presenta un buen manejo de rutas, incluye un servidor web de desarrollo y tiene un depurador y soporte integrado para pruebas unitarias.

Los frameworks :
-  Proporciona una estructura del proyecto
-  Facilita la colaboración
-  Es fácil encontrar librerias adaptadas al framework

## **¿Cómo instalar Flask?**
1. Activar el entorno virtual:
        
        source venv/bin/activate
2. Instalar Flask con pip:
   
        pip install flask
3.  Para comprobar su correcta instalación:
    
        flask --version

    O ver todas las dependencias instaladas:

        pip freeze
4. Ejecutar app.py:
        
        export FLASK_APP=app.py
        flask run
Y para guardar esas dependencias en un fichero **requirements.txt** (que luego nos permita ejecutarlo y instalarlo todo a la vez)

    pip freeze> requirements.txt


---

## **Dependencias utilizadas**

- **Flask_restful:** permite manejar de una manera más entendible las rutas.
  
- **Flask_pymongo** o **mongoengine**: para poder conectar con la bbdd
- **bcrypt:** para generar contraseñas




---
## **Instalación:**

- Para instalar todas las dependencias necessarias que hay en el **requiremetns.txt** en la venv:
        
        pip install -r requirements.txt
