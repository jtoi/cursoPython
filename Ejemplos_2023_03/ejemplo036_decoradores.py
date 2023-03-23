def externa(funcion_decorada):
    def interna():
        print("Antes de ejecutar la función")
        funcion_decorada()
        print("Después de ejecutar la función")

    return interna

@externa
def consumidor():
    print("Soy consumidor de decoradores")


consumidor()