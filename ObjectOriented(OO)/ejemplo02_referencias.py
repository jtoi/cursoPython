class Factura:
    def __init__(self, items : list):
        self.items = items


class Facturador(object):

    def __init__(self):
        pass

    def facturar(self, factura : Factura):
        valor=0
        for item in factura.items:
            valor += item.precior * item.unidades
        return(valor)

class Item:
    def __init__(self, nombre, unidades, precior):
        self.nombre = nombre
        self.unidades = unidades
        self.precior = precior


pan = Item("Pan",3, 0.80)
leche = Item("Leche",2, 1.20)
cerveza = Item("Cerveza",10, 0.70)

cesta = [pan, leche]
cesta.append(cerveza)


factura = Factura(cesta)
facturador = Facturador()

print(facturador.facturar(factura))