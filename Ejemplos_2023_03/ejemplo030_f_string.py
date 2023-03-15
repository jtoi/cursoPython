#dada una lista de números, mostrar todos los valores
#justificados a la derecha

lista = [10,10000,505,3]

for i in lista:
    print(f"{i:10}")


ancho_max = len(str(max(lista)))
for i in lista:
    print(f"{i:{ancho_max}}")

lista = ['Laura', 'Victor', 'David', 'Edu']
for i in lista:
    print(f"{i:10}*")


ventas = [("Primavera",500,200,100,800),("Verano",2500,3000,)]