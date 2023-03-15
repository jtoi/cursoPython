class Maquina:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    def __str__(self) -> str:
        return("str " + self.nombre + str(self.peso))   

    def __repr__(self) -> str:
        return("repr " + self.nombre + str(self.peso))
    
coche = Maquina("coche", 100)
print(coche)
print(r"{coche}")