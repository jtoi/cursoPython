class GestorPersonas:
    def __init__(self):
        self.personas = dict()
        self.add_persona(GestorPersonas.Persona("Persona1", "p1@gmail.com"))
        self.add_persona(GestorPersonas.Persona("Persona2", "p2@gmail.com"))
        self.add_persona(GestorPersonas.Persona("Persona3", "p3@gmail.com"))

    def add_persona(self, p : "Persona"):
        self.personas[p.nombre] = p.email

    def get_email(self, nombre):
        try:
            email = self.personas[nombre]
            return email
        except KeyError as ke:
            raise ke
    
    class Persona:
        def __init__(self, nombre, email):
            self.nombre = nombre
            self.email = email




