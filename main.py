from reportlab.lib.pagesizes import LETTER, A4
from reportlab.lib.units import inch, cm
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import red
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from pathlib import Path
import os

if Path('text_file2.pdf').is_file():
    os.remove('text_file2.pdf')

#Ширина отступа рамки
w_i = 0.5

a_4 = A4

# Настройка страницы какой тип бумаги!
canvas = Canvas("text_file2.pdf", pagesize=A4)

#Настройка шрифта
pdfmetrics.registerFont(TTFont('Times New Roman', 'Times New Roman.ttf'))
canvas.setFont("Times New Roman", 16)

canvas.setFillColor(red)
canvas.drawString(2 * inch, 8 * inch, "Привет.")

#Отрисовка рамки
canvas.line(w_i*cm, a_4[1]-w_i*cm, a_4[0]-w_i*cm, a_4[1]-w_i*cm)
canvas.line(w_i*cm, w_i*cm, w_i*cm, a_4[1]-w_i*cm)
canvas.line(w_i*cm, w_i*cm, a_4[0]-w_i*cm, w_i*cm)
canvas.line(a_4[0] - w_i*cm, w_i*cm, a_4[0] - w_i*cm, a_4[1]-w_i*cm)
# canvas.line(2*cm,723,580,723)

print(LETTER, A4)
#Если нужен второй шрифт
canvas.setFont("Times New Roman", 28)
canvas.drawString(2 * inch, 5 * inch, "Ололо.")

canvas.drawInlineImage("p.png", 2 * inch, 5 * inch)

canvas.save()