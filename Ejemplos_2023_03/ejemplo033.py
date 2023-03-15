planeta = 'Saturno'
print("*" + planeta.rjust(10) + "*")
print("*" + planeta.ljust(10) + "*")
print("*" + planeta.center(10) + "*")
print("*" + planeta.zfill(10) + "*")

nombre = "Agustina"
lenguaje = "Java"
cadena = "me llamo %s y programo en %s" % (nombre, lenguaje)
print(cadena)