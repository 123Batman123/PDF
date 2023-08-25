from reportlab.lib.pagesizes import LETTER, A4
from reportlab.lib.units import inch, cm
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.colors import red
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.platypus import SimpleDocTemplate, Image

from reportlab.platypus import Table

from reportlab.platypus import TableStyle
from reportlab.lib import colors

from pathlib import Path
import os



if Path('top.pdf').is_file():
    os.remove('top.pdf')
###########################################################
pdfmetrics.registerFont(TTFont('Free_sans', 'fonts/Times New Roman.ttf'))
###########################################################
i = Image('p.png')
i.drawHeight = 100
i.drawWidth = 100

data = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],

]
###########################################################
file = 'top.pdf'
pdf = SimpleDocTemplate(
    file,
    pagesize=A4
)
###########################################################
table = Table(data, spaceBefore=500, colWidths=50, rowHeights=50,)
###########################################################
style = TableStyle([

    ('BACKGROUND', (0, 0), (3, 0), colors.green),
    ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Free_sans'),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('BOTTOMPADING', (0, 0), (-1, 0), 100),
])

table.setStyle(style)

ts = TableStyle([
    ('BOX', (0, 0), (-1, -1), 1, colors.black),
    # ('SPAN', (0, 0), (1, 1)),
    # ('LINEBEFORE', (0, 0), (-1, -1), 1, colors.black),
    # ('LINEABOVE', (0, 0), (-1, -1), 1, colors.black),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
])

table.setStyle(ts)

elems = []
elems.append(table)
# elems.append(table)

pdf.build(elems)
