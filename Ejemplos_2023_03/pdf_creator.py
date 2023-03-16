from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader

def create_canvas(doc_title):
    cv = canvas.Canvas(f"{doc_title}.pdf", pagesize=A4)
    return cv


def setValores(cv, valores):
    tope = 500
    inc = i = total = 0
    spc = " "
    cv.setFont("Courier", 15)
    for linea in (valores):
        precio = '{0:.2f}'.format(linea[2])
        valor = '{0:.2f}'.format(linea[2]*linea[1])
        total += linea[1]*linea[2]
        # print(valor)
        i += 1
        cv.drawString(0, tope+inc, f"{i:>4} {spc:>2} {linea[0]:<10}")
        cv.drawString(396, tope+inc, f"{linea[1]}{precio:>8}€{valor:>9}€")
        # cv.drawString(416, tope+inc, f"{precio:>10}")
        # print(f"{precio:>10} {valor:>20}",end='')
        # cv.drawString(484, tope+inc, f"{valor:>12}")
        inc -= 27
    
    iva = '{0:.2f}'.format(total+total*0.12)
    total = '{0:.2f}'.format(total)
    cv.drawString(430, 90, f"Total: {total:>7}€")
    cv.drawString(447, 45, f"IVA: {iva:>7}€")
    print(total)


def drawFooter(cv):
    cv.setFont("Helvetica", 10)
    cv.drawString(40, 60, f"Elaborado por:")
    cv.drawString(200, 60, f"Recibido por:")
    cv.setFont("Helvetica", 15)
    cv.drawString(100, 40, "Julio Toirac")
    cv.drawString(250, 40, "Fernando Paniagua")



def draw_header(cv, dato):
    enc = 720
    cv.setFont("Times-Roman", 30)
    cv.drawString(50, 780, "Factura")
    cv.setFont("Times-Roman", 20)
    cv.drawString(50, enc, f"{dato[0]:<30}")
    cv.setFont("Times-Roman", 12)
    cv.drawString(50, enc-20, f"{dato[1]:<30}")
    cv.drawString(50, enc-40, f"{dato[2]:<30}")
    cv.setFont("Times-Roman", 16)
    cv.drawString(30, 575, f"Nº")
    cv.drawString(150, 575, f"Descripción")
    cv.drawString(387, 575, f"Qtty")
    cv.drawString(438, 575, f"Precio")
    cv.drawString(510, 575, f"Valor")


def draw_logo(cv):
    logo = ImageReader('logo.jpg')
    cv.drawImage(logo, 330, 650, mask='auto')


def draw_lines(cv):
    cv.line(23, 825, 23, 23)
    cv.line(23, 23, 573, 23)
    cv.line(573, 23, 573, 825)
    cv.line(573, 825, 23, 825)
    
    cv.line(23, 600, 573, 600)
    cv.line(23, 560, 573, 560)

    cv.line(60, 600, 60, 70)
    cv.line(380, 600, 380, 70)
    cv.line(420, 600, 420, 23)
    cv.line(490, 600, 490, 23)

    cv.line(23, 70, 573, 70)
    cv.line(420, 117, 573, 117)
    cv.line(200, 70, 200, 23)


def drawFooter(cv):
    cv.setFont("Helvetica", 10)
    cv.drawString(35, 60, f"Elaborado por:")
    cv.drawString(230, 60, f"Recibido por:")
    cv.setFont("Helvetica", 15)
    cv.drawString(70, 40, "Julio Toirac")
    cv.drawString(250, 40, "Fernando Paniagua")




def save_canvas(cv):
    cv.save()

