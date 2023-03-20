class Humano:
    esperanza_de_vida=85
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola soy {self.nombre}")


adan = Humano("Adán")
eva = Humano("Eva")
adan.saludar()
eva.saludar()
print(Humano.esperanza_de_vida)
print(adan.esperanza_de_vida)
print(eva.esperanza_de_vida)
eva.esperanza_de_vida=100 #peligro crea atributo que hace sombra al atributo esperanza_de_vida de la clase
print(eva.esperanza_de_vida)
Humano.esperanza_de_vida=90
print(adan.esperanza_de_vida)
print(eva.esperanza_de_vida)
print(Humano.esperanza_de_vida)
Humano.numero_de_hijos_potenciales = 10 #Construcción de atributo de clase en tiwempo de ejecución
