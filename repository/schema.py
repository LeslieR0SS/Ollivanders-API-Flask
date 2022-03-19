from mongoengine import *

class Ollivanders(Document):
    name = StringField(required=True)
    sell_in = IntField(required=True)
    quality = IntField(required=True)
    
    def get_name(self):
        return self.name
    
    def get_sell_in(self):
        return self.get_sell_in
    
    

    def to_json(self):
        return {"name": self.name, "sell_in": self.sell_in, "quality": self.quality}