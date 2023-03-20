#Crear una clase Persona

class Persona:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo
   
    def get_dinero(self, cant):
        try:
           self.__saldo -= cant
           if self.__saldo < 0:
               raise Exception("Saldo insuficiente")
           return self.__saldo
        except Exception as e:
            return e
       

julio = Persona("Julio", 1000)
print(julio.get_saldo())
print(julio.get_dinero(100))
print(julio.get_dinero(1000))
