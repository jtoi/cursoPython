class Vehiculo:
    
    def __init__(self, plazas, consumo, precio):
        self.plazas = plazas
        self.consumo = consumo
        self.precio = precio

    def __eq___(self, other):
        return self.plazas == other.plazas

v1 = Vehiculo(4,7,15000)
v2= Vehiculo(4,7,18000)
print(v1==v2) # Compara a través del método __eq__
print(v1 is v2)