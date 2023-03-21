class Animal:
    def __init__(self, nombre, estado_conservacion):
        self.nombre = nombre
        self.estado = estado_conservacion

    def get_estado_conservacion(self):
        return self.get_estado_conservacion
    
class AnimalAndarin(Animal):
    def __init__(self, nombre, estado_conservacion, numero_patas):
        super().__init__(nombre, estado_conservacion)
        self.numero_patas = numero_patas


class AnimalSaltarin(AnimalAndarin):
    def __init__(self):
        pass

perro= AnimalAndarin("Perro", "Sin Peligro", 4)
print(perro.nombre)
print(perro.estado)
print(perro.get_estado_conservacion())
print(perro.numero_patas)

#Función isinstance --> determina si un objeto es instancia de una clase
print(isinstance(perro, AnimalAndarin))
print(isinstance(perro, Animal))
print(isinstance(perro, list))

#Funcion issubclass --> Determina si una clase es hija de otra
print(issubclass(AnimalAndarin, Animal))
print(issubclass(Animal, AnimalAndarin))
print(issubclass(Animal, object))

#Herencia de 3 niveles
saltamontes = AnimalSaltarin()
print(isinstance(saltamontes, AnimalSaltarin))
print(isinstance(saltamontes, AnimalAndarin))
print(isinstance(saltamontes, Animal))
print(isinstance(saltamontes, object))