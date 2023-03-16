class Curso:
    
    def __init__(self, titulo:str, entidad:str, nhoras:int, expd:str):
        # Atributos
        self.titulo = titulo
        self.entidad = entidad
        self.nhoras = nhoras
        self.expd = expd

    def salva(self):
        with open('cursos.txt', 'a') as f:
            f.write(f'{self.titulo}, {self.entidad}, {self.nhoras} {self.expd}\n')
        

    def calularCoste(self, costHora):
        return self.nhoras * costHora


class Alumno:
    
    def __init__(self, nombre, dp, dni, email):
        # Atributos
        self.nombre = nombre
        self.dp = dp
        self.dni = dni
        self.emal = email
        self.estadoCivil = 'Soltero' #Creación de atributos ajeno a los argumentos de la clase

    def darseBaja(self, motivo, fecha):
        print(f'El alumno {self.nombre} ha sido bajado en la fecha {fecha} por el motivo: {motivo}')

    def darseAlta(self, fecha):
        print(f'El alumno {self.nombre} ha sido alta en la fecha {fecha}')

    def firmarAsistencia(self, fecha):
        print(f"El alumno {self.nombre} ha firmado la asistencia en la fecha {fecha}")

    def __str__(self) -> str:
        return f'Nombre: {self.nombre}, Dirección: {self.dp}, DNI: {self.dni}'
        
    
# laura = Alumno('Laura', 'Zaragoza', '123456789F', email='lyhxr@example.com') #Instanciamos la clase
# laura.darseAlta("16/03/2023")
# laura.firmarAsistencia("16/03/2023")
# laura.darseBaja("Me aburro en el curso", "17/03/2023")
# print(laura)


python = Curso('Python', 'CTI', 100, '1')
python.salva()
print(python.calularCoste(20))
excell = Curso('Excell', 'INAEM', 58, '2E-3')
excell.salva()