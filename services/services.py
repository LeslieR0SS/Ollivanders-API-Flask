from flask import jsonify, g
from repository.connection import get_bd
from repository.schema import Ollivanders
from mongoengine.queryset.visitor import Q

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
        
    
