import getpass
import hashlib
import datetime

class Credencial:
    def __init__(self, fichero, otro):
        self.fichero = fichero
        self.otro = otro
        self.hash = ''
    
    def get_digest(self, pas):
        m = hashlib.sha256()
        m.update(pas.encode())
        return m.hexdigest()
    
    def leeficHash(self):
        with open(self.fichero, 'r') as f:
            hash = f.read()
        self.hash = hash
        return hash

    def leeficContr(self):
        with open(self.otro, 'r', encoding="utf-8") as f:
            while True:
                palabra = f.readline()
                if not palabra:
                    print("Fin del fichero")
                    break
                palabra = palabra.replace('\n', '')
                if self.get_digest(palabra).upper() == self.hash.upper():
                    print(f"La palabra es: {palabra}")
                    break



if __name__ == "__main__":
    inicio = datetime.datetime.now().microsecond
    hash = Credencial('fernandopaniagua.txt', 'palabras_todas.txt')
    hash.leeficHash()
    hash.leeficContr()
    fin = datetime.datetime.now().microsecond - inicio
    print(f"Tiempo de ejecución: {fin/100000} microsegundos")
