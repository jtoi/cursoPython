def traductor(idioma):
    diccionario = {"ruso": {"perro": "собака", "vodka":"водка", "plaza":"квадрат"}, 
                    "chino":{"perro": "狗", "vodka":"伏特加酒", "plaza":"正方形"}}
    def decorador(funcion):
        def wrapper(palabra):
            funcion(diccionario[idioma][palabra])
    return decorador


@traductor
def sumar(*args):
    print("loquesea")


sumar(3,5,8,810,15,18,20)