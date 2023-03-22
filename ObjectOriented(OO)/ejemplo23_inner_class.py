class CV: # Outer class
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.contacto = CV.Contacto(email, telefono)

    """
        def __init__(self, nombre, contacto: Contacto):
            self.nombre = nombre
            self.contacto = contacto

    """

    class Contacto: # Inner class
        def __init__(self, email, telefono):
            self.email = email
            self.telefono = telefono


cv1 = CV("nombre", "email1", "telf1")
contacto1 = CV.Contacto("email2", "telf2")