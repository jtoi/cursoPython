from Levenshtein import distance

# nombre_director = input("Ingrese el nombre de director: ")

# fichero = open("./directores.txt", "r", encoding="utf-8")

# masCerca = 100
# nombre_sale=''
# while True:
#     director = fichero.readline().replace('\n', '')
#     if director == "":
#         break
#     distancia = distance(nombre_director, director)
#     if distancia < masCerca:
#         nombre_sale=director
#         masCerca = distancia

# print(masCerca)
# print(nombre_sale)

# fichero.close()

def get_directores():
    fichero = open("./directores.txt", "r", encoding="utf-8")
    directores = [director.replace('\n', '') for director in fichero.readlines()]
    fichero.close()
    return directores

def get_candidato(lista_directores, director_buscado):
    candidato = lista_directores[0]
    for director in lista_directores:
        if(distance(director, director_buscado) < distance(candidato, director_buscado)):
            candidato = director
            
    return candidato


if __name__ == "__main__":
    dir_a_buscar = input("Ingrese el nombre del director a buscar: ")
    candidato = get_candidato(get_directores(), dir_a_buscar)
    print(f"La mejor sugerencia es {candidato}")