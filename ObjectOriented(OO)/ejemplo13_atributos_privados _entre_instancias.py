class Persona:
    
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.__saldo = saldo


    def get_saldo(self):
        return self.__saldo
    

    def set_saldo(self, nuevo_saldo):
        self.__saldo = nuevo_saldo
        return 
    

    def __mostrar_secreto(self):
        pass
    

    def mostrar_info(self):
        print(f"Soy {self.nombre} y tengo {self.__saldo} euros")


    def coger_dinero(self,otra_persona):
        self.saldo += 1000
        otra_persona.__saldo -= 1000
        otra_persona.MOSTRARSo() + 1




cristian = Persona("Cristian", 5000)
fernando = Persona("Fernando", 100)
cristian.mostrar_info()
fernando.mostrar_info()
fernando.coger_dinero(cristian)
cristian.mostrar_info()
fernando.mostrar_info()

