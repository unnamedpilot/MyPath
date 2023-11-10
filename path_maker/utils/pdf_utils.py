# pdf_utils.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.units import inch
from io import BytesIO

def generate_pdf(data_list):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    styles = getSampleStyleSheet()
    # Crear un estilo de párrafo con ajuste automático de línea y posiblemente un margen derecho
    style = styles['Normal']
    style.wordWrap = 'CJK'  # Esta propiedad ayuda a manejar el ajuste automático de palabras largas

    y_position = height - 40  # Iniciar desde la parte superior de la página.

    for item in data_list:
        name = item['name']
        description = item['description']

        # Dibujar el nombre del lugar
        p_name = Paragraph(name, style)
        w_name, h_name = p_name.wrap(width - 80, y_position)  # 40 unidades de margen a cada lado
        p_name.drawOn(c, 40, y_position - h_name)  # Dibuja el nombre en el canvas
        y_position -= h_name + 10  # Añadir un pequeño margen entre el nombre y la descripción

        # Dibujar la descripción del lugar
        p_desc = Paragraph(description, style)
        w_desc, h_desc = p_desc.wrap(width - 80, y_position)  # 40 unidades de margen a cada lado
        if y_position < h_desc + 40:
            c.showPage()
            y_position = height - 40
            p_desc.wrapOn(c, width - 80, height - 80)  # Reajustar para la nueva página
        p_desc.drawOn(c, 40, y_position - h_desc)
        y_position -= h_desc + 20  # Añadir un margen entre las descripciones

        # Evitar escribir fuera del margen inferior de la página.
        if y_position < 40:
            c.showPage()
            y_position = height - 40

    c.save()
    buffer.seek(0)
    return buffer
