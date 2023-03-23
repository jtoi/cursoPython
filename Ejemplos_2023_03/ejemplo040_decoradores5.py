def validador(funcion):
    def funcion_interna(*args):
        if "chucho" in args:
            raise Exception("No admitimos la palabra chucho")
        else:
            function(*args)
    return funcion_interna


@validador
def mostrar(*args):
    for arg in args:
        print(arg)


mostrar("perro", "chucho", "animal", "mascota")