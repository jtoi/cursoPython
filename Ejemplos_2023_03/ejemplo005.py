with open("datos.txt", "r", encoding="utf-8") as fichero:
    while True:
        x = fichero.readline().replace('\n', '')
        """
        if x=="":
            print("FIN")
            break
        """
        if x=="": print("FIN"); break
        print(x)#Victor dice linea1
   
with open("datos.txt", "r", encoding="utf-8") as fichero:
    lineas = fichero.readlines()

    #variante 1
    salida = list()#
    for palabra in lineas:
        salida.append(palabra.replace('\n', ''))
    print(salida)

    #variante 2
    lineas_copia = lineas[:]
    for i in range(len(lineas)):
        lineas_copia[i] = lineas_copia[i].replace('\n', '')
    print(lineas_copia)

    #variante 3
    salida = [linea.replace('\n', '') for linea in lineas]
    print(salida)
