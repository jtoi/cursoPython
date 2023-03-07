

def leerFichero(nombre : str) -> str:
    fichero = open(nombre, "r")
    info = fichero.read()
    fichero.close()
    print(info)

if __name__ == "__main__":
    contenido = leerFichero("ejemplo001.py")
    print(contenido)