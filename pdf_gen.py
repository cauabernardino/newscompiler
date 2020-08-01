from fpdf import fpdf, FPDF
from datetime import date, datetime
import os


fpdf.set_global("SYSTEM_TTFONTS", os.path.join(os.path.dirname(__file__),'fonts'))


def pdf_gen(search_term, lines):
    # Date and term concatenation
    today = str(date.today())
    today_edit = date.today().strftime('%d/%B/%Y')
    term = search_term.upper()
    filename = " ".join((today, term))
    
    # File creation
    pdf = FPDF(unit='mm', format='A4')
    
    # Font adition
    pdf.add_font("Open Sans", style="", fname="OpenSans-Regular.ttf", uni=True)
    pdf.add_font("Open Sans", style="B", fname="OpenSans-Bold.ttf", uni=True)
    pdf.add_font("Open Sans", style="I", fname="OpenSans-Italic.ttf", uni=True)
    pdf.add_font("Open Sans", style="BI", fname="OpenSans-BoldItalic.ttf", uni=True)

    # Page creation
    pdf.add_page()
    pdf.set_font("Open Sans", 'B', size=12)
    pdf.cell(200, 10, txt=f"News for {term} on {today_edit}", ln=1, align="C")
    
    # News addition
    count = 1
    pdf.set_font("Open Sans", '', size=10)
    for i in range(len(lines)):
        line = f"{count}) {lines[i][0]}\nLink: {lines[i][1]}"
        pdf.multi_cell(0, 10, line, 1, 1)
        count += 1

    # Output
    pdf.output(".".join((filename,"pdf")), 'F')
