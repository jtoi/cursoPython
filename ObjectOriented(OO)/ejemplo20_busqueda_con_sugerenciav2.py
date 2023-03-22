from Levenshtein import distance

class Director:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__distancia = 0

    def set_distacia(self, candidato):
        self.__distancia = distance(self.nombre, candidato)

    def __lt__(self, other):
        return self.__distancia < other.__distancia
    
    def __repr__(self):
        return self.nombre
    



def get_directores():
        fichero = open("./directores.txt", "r", encoding="utf-8")
        directores = [Director(director.replace('\n', '')) for director in fichero.readlines()]
        fichero.close()
        return directores

def calcular_distancia(lista_directores, candidato):
    for director in lista_directores:
        director.calcular_distancia(candidato)


if __name__ == "__main__":
    directores = get_directores()
    candidato = input("Ingrese el nombre del director: ")
    calcular_distancia(directores, candidato)
    directores_ordenados = sorted(directores)
    print(directores_ordenados)