from reportlab.pdfgen import canvas


#pip install reportlab
nombre_cliente="Hotel Principal S.L."
direccion="Avda. de Barcelona, 18"
cif = "B50176938"
conceptos = (
    ("Alojamiento",5,110),
    ("Restaurante",1,50),
    ("Restaurante",1,5),
    ("Aparcamiento",5,10),
    ("Lavandería",2,5)
)
#Generar una factura en PDF
#https://recursospython.com/guias-y-manuales/crear-documentos-pdf-en-python-con-reportlab/

#Nivel 2
#Crear la factura obteniendo los datos del fichero ejemplo_35_datos_facturacion.dat
sp=' '

print("*"*82)
print(f"*{nombre_cliente:^40}*",end="")
print(" "*40,end="")
print("*")
print(f"*{direccion:^40}*",end="")
print(f" "*40,end="")
print("*")
print(f"*{cif:^40}*",end="")
print(f" "*40,end="")
print("*")
print("*"*82)



# with open("ejemplo_35_datos_facturas.dat","r") as datos:
#     datos = datos.readlines()

    

# print(datos)