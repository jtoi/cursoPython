from ITraductor import ITraductor


class Traductor_es_eng(ITraductor):
    def traducir(self,texto):
        print("Traduciendo de español a inglés")