from flask import jsonify, g
from repository.connection import get_bd
from repository.schema import Ollivanders
from controller.create_item import create_item

# from controller.create_item_object import create_item_object


class atlas:
    @staticmethod
    def get_items(db, url):
        db = get_bd(db, url)
        items_list = []
        for item in g.Ollivanders.objects():
            items_list.append(item.to_json())
        if len(items_list) > 0:
            return jsonify({"items": items_list})
        else:
            return jsonify({"items": "N/A"})

    @staticmethod
    def get_items_by_name(db, url, name):
        db = get_bd(db, url)
        items_list = []
        for item in g.Ollivanders.objects():
            item_obj = item.to_json()
            if item_obj["name"].lower() == name.lower():
                items_list.append(item_obj)
        if len(items_list) > 0:
            return jsonify({"items": items_list})
        else:
            return jsonify({"items": "N/A"})

    @staticmethod
    def create_item(db, url, newItem):
        db = get_bd(db, url)
        Ollivanders(
            name=newItem["name"], sell_in=newItem["sell_in"], quality=newItem["quality"]
        ).save()
        # los tres campos son obligatorios

    @staticmethod
    def delete_item(db, url, item_to_delete):
        db = get_bd(db, url)
        item_list = []
        for item in g.Ollivanders.objects():  # Objeto de la coleccion
            item_obj = item.to_json()  # Diccionario
            if (
                item_obj == item_to_delete
            ):  # para porceder a eliminaar el item requiere que ambos diccionarios tengan los mismo campos.
                item_list.append(item)  # aqui guardamos el documento/objeto de la bbdd
            else:
                continue
        if len(item_list) > 0:
            item_list[0].delete()

    @staticmethod
    def update_item(db, url):  # actualizamos todos los items iguales
        db = get_bd(db, url)
        for item in g.Ollivanders.objects():
            item_obj = item.to_json()

    @staticmethod
    def update(db, url):
        """
        -Del objeto de BD lo pasas a objeto PY
        -Actualizas el objeto PY
        -El objeto de BD no lo has actualizado
        -Al objeto de BD le modificas los datos sell_in y quality para que sean igual al del objeto PY
        -Actualizas el objeto de BD
        """
        db = get_bd(db, url)
        for item in g.Ollivanders.objects():
            item_data = (
                item.to_json()
            )  # esto nos devuelve el diccionario con los datos de la bbdd
            item_type = create_item(item_data)  # Objeto_BD -> Objeto_PY
            item_type.update_quality()  # aplicamos la lógica del dominio
            item.set_quality(item_type.quality)
            item.set_sell_in(item_type.sell_in)
            item.save()
