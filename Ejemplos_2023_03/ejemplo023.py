
def mayusculasr(palabra):
    return palabra.upper()


palabras = ["hola", "mundo", "hola mundo"]
palabrasCambiadas = list(map(mayusculasr, palabras))

print(palabrasCambiadas)

#variante condensada con lambda
palabrasCambiadas2 = list(map(lambda w: w.upper(), palabras))
print(palabrasCambiadas2)