#ejemplo Normal
temporada = ['primavera', 'verano', 'otoño', 'invierno']
ingresos = [10_000, 15_000, 20_000, 1_500]
zip_vetas = zip(temporada, ingresos)
lista_ventas = (list(zip_vetas))
for venta in lista_ventas:
    print(venta)


#ejemplo Normal con listas distitos tamaños
temporada = ['primavera', 'verano', 'otoño', 'invierno', 'entretiempo']
ingresos = [10_000, 15_000, 20_000, 1_500]
zip_vetas = zip(temporada, ingresos)
lista_ventas = (list(zip_vetas))
for venta in lista_ventas:
    print(venta)


#ejemplo Normal con listas distitos tamaños
temporada = ['primavera', 'verano', 'otoño', 'invierno', 'entretiempo']
ingresos = [10_000, 15_000, 20_000, 1_500]
zip_vetas = zip(temporada, ingresos, strict=True) #provoca error cuando no son iguales
lista_ventas = (list(zip_vetas))
for venta in lista_ventas:
    print(venta)

