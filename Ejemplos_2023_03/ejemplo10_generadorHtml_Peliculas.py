

#bug de Star Wars
def limpiarTitulo(titulo):
    caracteresK = ":?*"
    for caracter in caracteresK:
        titulo = titulo.replace(caracter, "")
    return titulo

def generarDocumentoHtml(titulo, poster,director):
    try:
        with open(limpiarTitulo(titulo)+".html", 'w', encoding="utf-8") as fichero:
            fichero.write("<html><head></head><body>")
            fichero.write("<h1>"+titulo+"</h1>")
            fichero.write("<img src=\""+poster+"\" width=\"200px\">")
            fichero.write("<p>Director: "+director+"</p>")
            fichero.write("")
            fichero.write("<body></html>")
            fichero.close()
    except BaseException as e:
        print(e)

