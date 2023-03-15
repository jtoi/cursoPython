from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.utils import ImageReader


def create_canvas(doc_title):
    cv = canvas.Canvas(f"{doc_title}.pdf", pagesize=A4)
    return cv


def draw_header(cv, nombre_cliente):
    cv.setFont("Times-Roman", 30)
    cv.drawString(50, 780, "Factura")
    cv.setFont("Times-Roman", 20)
    cv.drawString(50, 750, f"{nombre_cliente:>50}")


def draw_logo(cv):
    logo = ImageReader('logo.jpg')
    cv.drawImage(logo, 400, 685, mask='auto')


def draw_lines(cv):
    cv.line(50, 700, 50, 50)
    cv.line(350, 700, 350, 50)
    cv.line(420, 700, 420, 50)
    cv.line(480, 700, 480, 50)
    cv.line(420, 700, 420, 50)
    cv.line(420, 700, 420, 50)
    cv.line(420, 700, 420, 50)


def save_canvas(cv):
    cv.save()

