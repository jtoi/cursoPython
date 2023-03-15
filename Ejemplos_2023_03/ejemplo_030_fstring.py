#Dada una lista de números, mostrar todos los valores 
#alineados a la derecha
#print(f"El coste del trabajo es de {cantidad:20}€")

lista = [10,10000,505,3]
#Alinear a la derecha ocupando 10 caracteres
# for numero in lista:
#     print(f"{numero:10}")

#Alinear a la derecha ocupando el número de caracteres del valor más 'ancho'
# ancho_max = len(str(max(lista)))
# for numero in lista:
    
# ancho_max = len(str(max(lista)))
# for i in lista:
    # print(f"{i:{ancho_max}}")print(f"{numero:{ancho_max}}")

# lista = ["Laura","Víctor","David","Edu"]
# for nombre in lista:
    # print(f"{nombre:10}*")

#Crear una tabla 
# *PRIMAVERA    *VERANO    *OTOÑO     *INVIERNO     *
# *          500*        10*   1383913*        38343*
# *          500*        10*   1383913*        38343*
# *          500*        10*   1383913*        38343*
# *          500*        10*   1383913*        38343*
# *         2000*        40*
ventas=[
    ("Primavera",500,200,100,800),
    ("Verano",2500,3000,1000,50),
    ("Otoño",500,200,100,800),
    ("Invierno",2500,3000,1000,50)
    ]

#variante1
ventas_ordenadas = list(zip(ventas[0], ventas[1], ventas[2],ventas[3]))
for ventas in ventas_ordenadas:
    for i in ventas:
        print(f"{i:15}",end="")
    print()

#variante2
l = len(ventas[0])
for i in range[0,l]:
    print(f"{ventas[0][i]:15}",end="")




texto = 'Python'
#alinear a la derecha
print(f"*{texto:>10}")
#alinear a la izquierda
print(f"*{texto:<10}")

#centar
print(f"*{texto:^10}")

entero=10000
decimal=10.50
print(f"*{texto:10s}*")
print(f"*{entero:10d}*")
print(f"*{decimal:10f}*")