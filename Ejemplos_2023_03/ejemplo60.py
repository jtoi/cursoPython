lista = ["Lunes", "Martes", "Miércoles", "Jueves"]

def convertir(dia):
    return dia.upper()

# Utilizando map y lambda convertir todos los elementos de la lista a mayúsculas con la función convertir

lista_mayusculas = list(map(lambda x: x.upper(), lista)) # opción map con lambda



lista_emes = list(filter(lambda dia:dia.startswith("M"), lista))
# print(lista_mayusculas)
# print(lista_emes)

import mysql.connector

conexion = mysql.connector.connect(
    host = "localhost",
    port = 5672,
    user = "root",
    password = "sdfgsdfg"
)
