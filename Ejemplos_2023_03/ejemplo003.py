
def otro(nombre : str, contenido) -> str:
    #with es otra variante de apertura que no necesita el close
    with open(nombre, "w", encoding="utf-8") as fichero:
        fichero.write(contenido + " Se le agrega este pedazo para ver")
    return contenido

def abreFichero(nombre : str, contenido : str) -> str:
    try:
        fichero = open(nombre, "x", encoding="utf-8")
        fichero.write(contenido)
        fichero.close()
        return contenido
    except Exception:
        print("Ocurrió un error al abrirlo")
        return otro(nombre, contenido)
    



if __name__ == "__main__":
    contenido = abreFichero("ejemplo001.txt", "Este es una apertura de fichero")
    print(contenido)