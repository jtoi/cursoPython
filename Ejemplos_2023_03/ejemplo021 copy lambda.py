numeros = [3,8,10,1,4,15,20,21]
pares = filter(lambda numero: numero % 2 == 0, numeros)
print(list(pares))