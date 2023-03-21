class Vehiculo:
    def __init__(self, nombre):
        self.nombre = nombre

    def arrancar(self):
        print(f"Soy Vehiculo, mi nombre es {self.nombre} y estoy arrancando..")

    def avanzar(self):
        print(f"Soy Vehiculo, mi nombre es {self.nombre} y estoy avanzando...")


class VehiculoRodador(Vehiculo):
    def __init__(self, nombre):
        super().__init__(nombre)

    def arrancar(self):
        print(f"Soy VehiculoRodador, mi nombre es {self.nombre} y estoy arrancando..")

    def avanzar(self):
        super().avanzar()
        print(f"Soy VehiculoRodador, mi nombre es {self.nombre} y estoy avanzando...")


class Automovil(VehiculoRodador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def arrancar(self):
        print(f"Soy Automovil, mi nombre es {self.nombre} y estoy arrancando..")

    def avanzar(self):
        super().avanzar()
        print(f"Soy Automovil, mi nombre es {self.nombre} y estoy avanzando...")


v = Vehiculo("avion") 
v.arrancar()
v = VehiculoRodador("Algo")
v.arrancar()
v = Automovil("Seat")
v.arrancar()

v.avanzar()