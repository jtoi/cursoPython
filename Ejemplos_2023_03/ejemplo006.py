def traducir(palabra):
    diccionario = {"Perro": "Dog", "Barco": "Ship", "Casa": "House", "Manzana": "Apple"}
    return diccionario.get(palabra, "No exite")

lista = ["Perro","Barco","Casa","Manzana", "gato"]
salida = [traducir(linea) for linea in lista]
print(salida)