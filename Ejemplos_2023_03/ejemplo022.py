ciudades = [
    ("Zaragoza",666000),
    ("Albacete",173500),
    ("Guadalajara",84910)
]

def cuantificador(ciudad):
    return ciudad[1]

print(sorted(ciudades, key=cuantificador))

print(sorted())