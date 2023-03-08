def traducir(palabra):
    diccionario = {"Perro": "Dog", "Barco": "Ship", "Casa": "House", "Manzana": "Apple"}
    print(f"La palabra {palabra} se traduce como {diccionario[palabra]}")

lista = ["Perro","Barco","Casa","Manzana"]
salida = [traducir(linea) for linea in lista]