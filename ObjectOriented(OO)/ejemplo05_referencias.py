class Empresa(object):
    def __init__(self, nombre) -> None:
        self.nombre = nombre


class Holdign(object):
    def __init__(self, empresa:Empresa) -> None:
        self.empresa = empresa

    def modificar(self):
        self.empresa.nombre = self.empresa.nombre * 2


empresa1 = Empresa("Empresa 1")
holding1 = Holdign(empresa=empresa1)#empresa1 se pasa como referencia a la clase Holdign
holding1.modificar()
print(holding1.empresa.nombre)
print(empresa1.nombre)