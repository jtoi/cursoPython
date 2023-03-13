listado = [1,2,3,4,5,6,7,8,910,11]

def pares(lista):
    for i in lista:
        if i % 2 == 0:
            return i
        
pares = filter(pares, listado)

for i in pares:
    print(i)