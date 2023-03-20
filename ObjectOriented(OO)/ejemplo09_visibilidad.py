class Contrato:
    def __init__(self, nombre, salario, categoria):
        self.nombre = nombre #publico
        self._categoria = categoria #protegido
        self.__salario = salario #privada


    def get_salario(self): #forma de acceder a los atributos privados
        return self.__salario
    

    def set_salario(self, nuevo_salario): #forma de modificar atributos privados
        self.__salario = nuevo_salario



c = Contrato("Juan", 10000, "Médico")

print(c.nombre)
print(c._categoria)
# print(c.__salario) #no existe el atributo __salario da error
print(c._Contrato__salario)#trampa para acceder al atributo privado