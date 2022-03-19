from domain.types import *

tipos = {
    "ConjuredItem": ["Mariposa", "Scorpion", "ConjuredItem"],
    "NormalItem": ["Botella", "NormalItem", "Estrella"],
    "AgedBrie": ["Raton", "AgedBrie", "Pizza"],
    "Sulfuras": ["Noria", "Mascarilla", "Sufuras"],
    "Backstage": ["Pez", "Backstage"],
}


def create_item(item):  # item = {"name" : "Hola", "sell_in" : 45, "quality" : 27}
    for tipo in tipos:
        if item["name"] in tipos[tipo]:
            """
            Con el try-except evitamos un error en el supuesto caso que nosotros indiquemos
            un tipo de item que no tenemos programado en el dominio, convirtiéndolo de
            forma predeterminada en un NormalItem
            """
            try:
                return eval(
                    f"{tipo}({item['name']}, {item['sell_in']}, {item['quality']})"
                )
            except NameError:
                return NormalItem(item["name"], item["sell_in"], item["quality"])

    return NormalItem(item["name"], item["sell_in"], item["quality"])
