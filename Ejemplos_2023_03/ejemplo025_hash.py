import getpass
import hashlib

class Credencial:
    def __init__(self, id, pwd):
        self.id = id
        self.pwd = pwd
    
    def get_digest(self):
        m = hashlib.sha256()
        m.update(self.pwd.encode())
        return m.hexdigest()

    def __repr__(self):
        return f"{self.get_digest()}"

def registrar_usuario():
    id = input("Introduce identificador de usuario: ")
    pwd = getpass.getpass("Introduce contraseña: ")
    credencial = Credencial(id, pwd)
    return credencial

def guardaCredencial(credencial):
    fichero = open("contrasena.txt", "w")
    fichero.write(credencial.get_digest())
    fichero.close()

if __name__ == "__main__":
    credencial = registrar_usuario()
    guardaCredencial(credencial)
