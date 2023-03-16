import sys



class Empleado:
    
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"En el constructor de {self.nombre}")


    def __del__(self):
        print(f"En el destructorr de {self.nombre}")


e1 = Empleado('e1')
e2 = Empleado('e2')
e3 = Empleado('e3')
input("hit Enter para continuar")
e2 = None #Hace que se ejecute el destructor
input("hit Enter para continuar")
input("hit Enter para continuar")
sys.exit(0)