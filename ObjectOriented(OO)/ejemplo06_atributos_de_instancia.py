class Serie: 
        self.titulo = titulo
        self.num_temp = num_temp

    
    def set_director(self, director):
        self.director = director

   
    def mostrar_productora(self):
        print(self.productora)



strike = Serie("Strike", 4)
strike.set_director("Juan") #añadimos un atributo dentro del método
strike.productora = 'HBO' #añadimosun atributo fuera de la clase
print(dir(Serie))
print(dir(strike))
strike.mostrar_productora()


the_last_of_us = Serie('The Last of Us', 2)
print(the_last_of_us.mostrar_productora()) #da error porque se está llamando un atributo que no ha sido creado
