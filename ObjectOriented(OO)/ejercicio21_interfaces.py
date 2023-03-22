class IEnemigo:
    def caminar(self):
        raise NotImplementedError()
    
    def saltar(self):
        raise NotImplementedError()
    
    def atacar(self):
        raise NotImplementedError()
    


class EnemigoSimple(IEnemigo):
    def caminar(self):
        print("Enemigo simple caminando")
    
    # def saltar(self):
    #     print("Enemigo simple saltando")
    
    def atacar(self):
        print("Enemigo simple atacando")
    


enemigo_simple = EnemigoSimple()
enemigo_simple.caminar()
enemigo_simple.atacar()
enemigo_simple.saltar()