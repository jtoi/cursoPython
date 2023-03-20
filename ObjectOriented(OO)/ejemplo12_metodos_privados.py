class Generador:
    def __init__(self, name):
        self.name = name


    def calcular_longitud(self):
        longitud = self.__metodo_oculto()
        return longitud


    def __metodo_oculto(self):
        l = len(self.name)
        return l
    
g = Generador("Ernesto")
print(g.calcular_longitud())
# g.__metodo_oculto() #provoca error