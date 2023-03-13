
class Factura:
    def __init__(self, id, importe) -> None:
        self.id = id
        self.importe = importe*2

    def __repr__(self):
        return f"Factura {self.id} con importe {self.importe}"
    
    def masDe2000(self):
        return self.importe > 1200

f1 = Factura(1, 1000)
f2 = Factura(2, 2000)   
f3 = Factura(3, 3000)

lista = [f1, f2, f3]

    

listado_Fact = list(filter(Factura.masDe2000, lista))

print(listado_Fact)