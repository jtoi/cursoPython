class PilaVaciaException(Exception):
    def __init__(self, *args: object):
        super().__init__(*args)

    def encender_sirena_luminosa(self):
        print("Encendiendo la sirena luminosa")

#CREAR UNA CLASE PILA QUE IMPLEMENTE UNA PILA

class PaniPila:
    def __init__(self):
        self.pila = []

    def push(self, valor):
        self.pila.insert(0,valor)
        print(self.pila)

    def pop(self):
        if len(self.pila) > 0:
            print(self.pila.pop(0))
            print(self.pila)
        else:
            raise PilaVaciaException("No hay elementos en la pila")
        


if __name__ == "__main__":
    lista = PaniPila()
    lista.push("8")
    lista.push("3")
    lista.push("6")
    lista.push("9")
    try:
        lista.pop()
        lista.pop()
        lista.pop()
        lista.pop()
        lista.pop()
        lista.pop()
    except PilaVaciaException as pve:
        pve.encender_sirena_luminosa()
    except Exception as e:
        print(e)

