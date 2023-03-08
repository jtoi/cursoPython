try:
    fichero = open("noexiste.txt", "r")
    fichero.read()
    fichero.close()
except FileNotFoundError:
    print("El fichero no existe")

try:
    with open("noexiste.txt", "r") as fichero:
        fichero.read()
except FileNotFoundError:
    print("El fichero no existe")