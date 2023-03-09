

#Copia un fichero entrado por el usuario a las 
#carpetas indicadas en la variable directorios


directorios = ["Ejemplos_2023_03/dir1", "Ejemplos_2023_03/dir2"]

def copiaFile(nombre):
    for directorio in directorios:
        f_entrada = open(f"Ejemplos_2023_03/{nombre}", "rb")
        f_salida = open(f"{directorio}/{nombre}", "wb")
        caracter = f_entrada.read(1)
        while caracter:
            f_salida.write(caracter)
            caracter = f_entrada.read(1)
        f_salida.close()
        f_entrada.close()
        



if __name__ == '__main__':
    nombre = input("Entre el nombre del fichero a copiar: ")
    copiaFile(nombre)
