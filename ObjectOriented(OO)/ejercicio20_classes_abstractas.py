from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    def arrancar(self):
        print("Arrancando")

    def parar(self):
        print("Parando")

    @abstractmethod
    def avanzar(self):
        pass

    @abstractmethod
    def retroceder(self):
        pass



class CocheOruga(Vehiculo):
    def avanzar(self):
        print("Soy un coche oruga")
    def retroceder(self):
        print("Soy un coche oruga retrocediendo")



micoche = CocheOruga("Kia")
micoche.avanzar()