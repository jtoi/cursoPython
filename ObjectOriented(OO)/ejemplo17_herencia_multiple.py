class MedioTransporte:
    def __init__(self, nombre):
        self.nombre = nombre
        print("Constructor de la clase MedioTransporte")
    def saludar(self):
        print("Hola soy Mediode Transporte")

class Avion(MedioTransporte):
    def __init__(self, nombre):
        print("Constructor de la clase Avion")
        super().__init__(nombre)
    def volar(self):
        print("Volando")
    def saludar(self):
        print("Hola soy Avion")


class Barco(MedioTransporte):
    def __init__(self, nombre):
        print("Constructor de la clase Barco")
        super().__init__(nombre)
    def navegar(self):
        print("Navegando..")
    def saludar(self):
        print("Hola soy Barco")


class Automovil(MedioTransporte):
    def __init__(self, nombre):
        print("Constructor de la clase Automovil")
        super().__init__(nombre)
    def rodar(self):
        print("Rodando")
    def saludar(self):
        print("Hola soy Automovil")


class Hovercraft(Barco, Automovil):
    def __init__(self, nombre):
        super().__init__(nombre)
        print("Constructor de la clase Hovercraft")
    def deslizar(self):
        print("Deslizando")


h = Hovercraft("Hovercraft")
h.deslizar()
h.navegar()
h.rodar()
print(h.nombre)
h.saludar()