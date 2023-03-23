import re

# texto = "2023-04-18 T28Z 1001 RODRIGUEZ"

# exp = "[A-Z][0-9]{2}[A-Z]"
# re_object = re.compile(exp)

# resultado = re_object.search(texto)
# if resultado is not None:
#     print(resultado.span())
#     pos = resultado.span()
#     print(texto[pos[0]:pos[1]])
# else:
#     print("No resultado")


# resultado = re_object.search(exp, texto)
# if resultado is not None:
#     print(resultado.span())
#     pos = resultado.span()
#     print(texto[pos[0]:pos[1]])
# else:
#     print("No resultado")


expr = r"[a-zA-Z]"
while True:
    palabra = input("introduce palabra: ")
    resultado = re.fullmatch(expr, palabra)
    if(resultado == None):
        print("No válido")
    else:
        print("Válido")
