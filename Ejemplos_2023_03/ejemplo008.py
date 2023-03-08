import json


def mostraTodo(serie):
    for k, v in serie.items():
        if (not isinstance(v, list)):
            print(k,":",v)
        else: 
            print("Actores")
            for elemento in v:
                for k2, v2 in elemento.items():
                    print(k2,":",v2)



def mostarOrdenado(serie):
    print(f"Titulo: {serie['titulo']}")
    print(f"Director: {serie['director']}")
    print(f"Temporadas: {serie['numeroTemporadas']}")
    for actor in serie['actores']:
        print(f"Actor: {actor['nombre']} Nacionalidad: {actor['nacionalidad']}")

fichero = open("datos.json", encoding="utf-8")
serie = json.load(fichero)
#print(type(serie))
#print(serie)


#mostraTodo(serie)
mostarOrdenado(serie)