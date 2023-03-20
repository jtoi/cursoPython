class Genero:
    def __init__(self, genero):
        self.__genero = genero

    def set_genero(self, genero):
        self.__genero = genero
    
    def get_genero(self):
        return self.__genero




class Pelicula(Genero):
    def __init__(self, titulo, director, genero, recaudacion, presupuesto):
        self.titulo = titulo
        self.director = director
        Genero(genero)
        self.genero = Genero.get_genero()
        self.__recaudacion = recaudacion
        self.presupuesto = presupuesto
        


    def get_recaudacion(self):
        return self.__recaudacion
    

    def set_recaudacion(self, recaudacion):
        self.__recaudacion = recaudacion


    def get_rentabilidad(self):
        return self.presupuesto - self.__recaudacion




el_marciano = Pelicula('El Marciano', 'Riddley Scott', 'Ciencia Ficcion', 30e6, 10e6)
print(el_marciano.get_rentabilidad)