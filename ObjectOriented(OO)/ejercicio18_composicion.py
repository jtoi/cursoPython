class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    def mostrar(self):
        print(f"Empleado: {self.nombre}")

class Departamento:
    def __init__(self, nombre, director):
        self.nombre = nombre
        self.director = director
        self.__empleados = []
    def mostrar(self):
        print(f"Departamento: {self.nombre}")
        print(f"Director: ",end='')
        self.director.mostrar()
        for empleado in self.__empleados:
            empleado.mostrar()

    def agregarEmpleado(self, empleado):
        self.__empleados.append(empleado)

class Empresa:
    def __init__(self, nombre, director):
        self.nombre = nombre
        self.director = director
        self.__departamentos = []
    def mostrar(self):
        print(f"Empresa: {self.nombre} - Director: {self.director}")

    def agregarDpto(self, departamento):
        self.__departamentos.append(departamento)

        
class Multinacional:
    def __init__(self, nombre, director):
        self.nombre = nombre
        self.director = director
    def mostrar(self):
        print(f"Multinacional: {self.nombre}")




victor = Empleado("Victor")
laura = Empleado("laura")
dpto_sistemas = Departamento("Sistemas", Empleado('Manuel'))
dpto_sistemas.agregarEmpleado(victor)
dpto_sistemas.agregarEmpleado(laura)
dpto_sistemas.mostrar()