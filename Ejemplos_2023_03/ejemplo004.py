def saludar(saludo, nombre="Victor"):
    print(saludo, nombre)

#saludar("Hola", "Miguel Angel")
#saludar("Hola")


fichero = open("elquijote.txt", "r", encoding="utf-8")
primeros19 = fichero.read(19) #primeros 19 caracteres
fichero.seek(11)
desdeEl5Al10 = fichero.read(8) #desde el 11 al 19
print(primeros19)
print(desdeEl5Al10)
fichero.close()