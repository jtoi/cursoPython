def sumar(s1, s2):
    raise NotImplementedError("Función no implementada")

def restar(r1,r2):
    if isinstance(r1,int) or isinstance(r2,int):
        raise TypeError
    return r1-r2

def dividir(d1,d2):
    if d2 == 0:
        raise ZeroDivisionError("El divisor no puede ser 0")

# sumar(1, 2)
#print(restar(1, 2))
dividir(6,0)