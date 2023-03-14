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

def get_id():
    with open('contrasena.txt', 'r') as fic:
        hash = fic.read()
    return hash.replace("\n", "")

if __name__ == "__main__":
    credencial = registrar_usuario()
    verif = get_id()
    if credencial.get_digest() == verif:
        print("Usuario ya registrado")
    else:
        print(f"|{credencial}| - las credenciales no coinciden |{verif}|")
