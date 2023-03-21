class Genero:
    def __init__(self, genero):
        self.genero = genero
    
    def get_genero(self):
        return self.genero




class Pelicula(Genero):
    def __init__(self, titulo, director, genero, recaudacion, presupuesto):
        self.titulo = titulo
        self.director = director
        pase = Genero(genero)
        self.genero = pase.get_genero()
        self.__recaudacion = recaudacion
        self.presupuesto = presupuesto

    def get_recaudacion(self):
        return self.__recaudacion
    

    def set_recaudacion(self, recaudacion):
        self.__recaudacion = recaudacion
    
    
    def mostrar_datos(self):
        print(f"{self.titulo}")


    def __calcular_rentabilidad(self):
        if self.presupuesto == 0:
            raise Exception("Alerte!!! El presupuesto es 0")
        return  self.__recaudacion / self.presupuesto
    
    def get_rentabilidad(self):
        return self.__calcular_rentabilidad()
        
    def __repr__(self) -> str:
        return f"{self.titulo} dirigida por {self.director} del género {self.genero} logró una rentabilidad de {self.__recaudacion - self.presupuesto}"


if __name__ == "__main__":
    terror = Genero("Terror")
    comerdia= Genero("Comédia")
    CF = Genero("Ciencia Ficción")

    el_marciano = Pelicula('El Marciano', 'Riddley Scott', CF, 30e6, 10e6)


    try:
        rentabilidad = el_marciano.get_rentabilidad()
        print(rentabilidad)
    except Exception as e:
        print(e)
