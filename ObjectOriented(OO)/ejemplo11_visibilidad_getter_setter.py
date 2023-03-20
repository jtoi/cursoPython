class Videojuego:
    def __init__(self, titulo, genero, precio):
        self.titulo = titulo
        self.__genero = genero
        self.__precio = precio

    def get_genero(self):
        return self.__genero
    
    def set_genero(self, nuevo_genero):
        self.__genero = nuevo_genero

    #uso decoradores
    @property
    def precio(self):
        print("En el get de precio (@property)")
        return self.__precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        print("En el set de precio (@precio.setter)")
        self.__precio = nuevo_precio



cod = Videojuego('Call of Dutty', 'FPS', 20)
print(cod.get_genero())
cod.set_genero('Plataformas')
print(cod.get_genero())
#acceso a los atributos privados como si fuesen públicos pero a través de métodos
print(cod.precio)
cod.precio = 30
print(cod.precio)