from mongoengine import *


class Ollivanders(Document):
    name = StringField(required=True)
    sell_in = IntField(required=True)
    quality = IntField(required=True)

    def get_name(self):
        return self.name

    def get_sell_in(self):
        return self.sell_in

    def set_sell_in(self, new_sell_in):
        self.sell_in = new_sell_in

    def get_quality(self):
        return self.quality

    def set_quality(self, new_quality):
        self.quality = new_quality

    def to_json(self):
        return {"name": self.name, "sell_in": self.sell_in, "quality": self.quality}
