"""
1- leer el fichero del quijote
2- obtener una lista con todas las palabras
3- convertir la lista a conjunto
4- pedir al usuario una palabra e indicarle si existe o no
EXTRA: No tenga en cuenta si las palabras están en mayúsculas o minúsculas
"""

def leerFichero(nombre : str) -> str:
    fichero = open(nombre, "r", encoding="utf-8")
    info = fichero.read()
    fichero.close()
    return info

def limpiarTexto(texto):
    simbolos = ".,_;-?¿!¡():"
    for simbolo in simbolos:
        texto = texto.replace(simbolo, "")
    return texto

def obtenerLista(texto):
    return texto.split(' ')


if __name__ == "__main__":
    contenido = leerFichero("elquijote.txt")
    contenido = limpiarTexto(contenido)
    palabras = obtenerLista(contenido)
    conjunto = set(palabras)

    palabraABuscar = input("Teclee la palabra a buscar: ")
    if palabraABuscar in conjunto:
        print(f"La palabra {palabraABuscar} si se encuentra!!!")
    else:
        print(f"La palabra {palabraABuscar} no se encuentra!!!")




