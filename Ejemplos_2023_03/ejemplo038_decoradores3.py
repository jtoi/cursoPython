def ruso(funcion_decorada):
    diccionario = {"perro": "собака", "vodka":"водка", "plaza":"квадрат"}
    def interna(nombre):
       funcion_decorada(diccionario.get(nombre))
    return interna

def chino(funcion_decorada):
    diccionario = {"perro": "狗", "vodka":"伏特加酒", "plaza":"正方形"}
    def interna(nombre):
       funcion_decorada(diccionario.get(nombre))
    return interna

@chino
def mostrar(palabra):
    print(f" {palabra}")


mostrar("vodka")