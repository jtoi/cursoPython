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
        print(f"Empresa: {self.nombre}")
        print(f"Director: ", end='')
        self.director.mostrar()
        for departamento in self.__departamentos:
            departamento.mostrar()

    def agregarDpto(self, departamento):
        self.__departamentos.append(departamento)

        
class Multinacional:
    def __init__(self, nombre, director):
        self.nombre = nombre
        self.director = director
        self.__empresas = []
    def mostrar(self):
        print(f"Multinacional: {self.nombre}")
        print(f"Director: ", end='')
        self.director.mostrar()
        for empresa in self.__empresas:
            empresa.mostrar()

    def agregarEmpre(self, empresa):
        self.__empresas.append(empresa)





victor = Empleado("Victor")
laura = Empleado("laura")
antonio = Empleado("Antonio")
maria = Empleado("María")
maricarmen = Empleado("Maricarmen")
david= Empleado("David")
javier= Empleado("Javier")
josefa= Empleado("Josefa")
dpto_sistemas = Departamento("Sistemas", Empleado('Manuel'))
dpto_sistemas.agregarEmpleado(victor)
dpto_sistemas.agregarEmpleado(laura)
# dpto_sistemas.mostrar()
dpto_desarrollo = Departamento("Desarrollo", Empleado('José'))
dpto_desarrollo.agregarEmpleado(antonio)
dpto_desarrollo.agregarEmpleado(maria)
# dpto_sistemas.mostrar()
empresa1 = Empresa("Empresa1", Empleado('Julio'))
empresa1.agregarDpto(dpto_sistemas)
empresa1.agregarDpto(dpto_desarrollo)

dpto_sistemas2 = Departamento("Sistemas", Empleado('Maria Pilar'))
dpto_sistemas2.agregarEmpleado(maricarmen)
dpto_sistemas2.agregarEmpleado(david)
# dpto_sistemas.mostrar()
dpto_desarrollo2 = Departamento("Desarrollo", Empleado('Juan'))
dpto_desarrollo2.agregarEmpleado(javier)
dpto_desarrollo2.agregarEmpleado(josefa)
# dpto_sistemas.mostrar()
empresa2 = Empresa("Empresa2", Empleado('Julio'))
empresa2.agregarDpto(dpto_sistemas2)
empresa2.agregarDpto(dpto_desarrollo2)

holding = Multinacional("Holding", Empleado('Francisco'))
holding.agregarEmpre(empresa1)
holding.agregarEmpre(empresa2)
holding.mostrar()