def externa(funcion_decorada):
    def interna(nombre):
        print(f"Antes de ejecutar la función {nombre}")
        funcion_decorada(nombre)
        print(f"Después de ejecutar la función {nombre}")

    return interna

@externa
def consumidor(nombre):
    print(f"Soy consumidor de decoradores {nombre}")


consumidor("Alicia")