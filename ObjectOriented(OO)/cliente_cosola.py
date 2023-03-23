from ejercicio25 import GestorPersonas as GP

nombre = input("Diga un nombre: ")

gp = GP()
try:
    email = gp.get_email(nombre)
    print(email)
except KeyError:
    print("KO", "El nombre no existe")

