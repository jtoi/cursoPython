


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

import pdf_creator

if __name__ == "__main__":
    cv = pdf_creator.create_canvas("prueba")
    pdf_creator.draw_header(cv, nombre_cliente)
    pdf_creator.draw_logo(cv)
    pdf_creator.draw_lines(cv)
    pdf_creator.save_canvas(cv)