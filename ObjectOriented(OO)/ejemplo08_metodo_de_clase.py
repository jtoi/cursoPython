class Serie:
    longitud_maxima = 10
    def __init__(self, titulo):
        self.titulo = titulo

    def cambiar_longitud_maxima(self):
        self.longitud_maxima += 1