import os
from fpdf import fpdf, FPDF

from newscompiler.tools import get_date


fpdf.set_global("SYSTEM_TTFONTS",
                os.path.join(os.getcwd(), 'fonts'))


def pdf_gen(search_term, lines):
    term = search_term.upper()
    filename = " ".join((get_date(), term))

    # File creation
    pdf = FPDF(unit='mm', format='A4')

    # Font adition
    pdf.add_font("Open Sans", style="", fname="OpenSans-Regular.ttf", uni=True)
    pdf.add_font("Open Sans", style="B", fname="OpenSans-Bold.ttf", uni=True)
    pdf.add_font("Open Sans", style="I", fname="OpenSans-Italic.ttf", uni=True)
    pdf.add_font("Open Sans", style="BI",
                 fname="OpenSans-BoldItalic.ttf", uni=True)

    # Page creation
    pdf.add_page()
    pdf.set_font("Open Sans", 'B', size=12)
    pdf.cell(
        200, 10, txt=f"News for {term} on {get_date(format=True)}", ln=1, align="C")

    # News addition
    count = 1
    pdf.set_font("Open Sans", '', size=10)
    for i in range(len(lines)):
        line = f"{count}) {lines[i][0]}\nLink: {lines[i][1]}"
        pdf.multi_cell(0, 10, line, 1, 1)
        count += 1

    # Output
    pdf.output(".".join((filename, "pdf")), 'F')
