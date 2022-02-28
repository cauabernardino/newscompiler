from pathlib import Path
from fpdf import fpdf, FPDF
from typing import List

from newscompiler.tools import get_date


FONT_NAMES = (
    ("OpenSans-Regular.ttf", ""),
    ("OpenSans-Bold.ttf", "B"),
    ("OpenSans-Italic.ttf", "I"),
    ("OpenSans-BoldItalic.ttf", "BI"),
)


def export_pdf(search_term: str, lines: List):
    """Handles the creation and exporting of news list into a PDF file.

    Args:
        search_term (str): The term that was searched.
        lines (List[Tuple[str, str]]): List of tuples with

    Returns:
        A PDF file in the package root directory.
    """
    term = search_term.upper()
    filename = " ".join((get_date(), term))

    # File creation
    pdf = FPDF(unit="mm", format="A4")

    # Font adition
    font_path = Path(__file__).resolve().parent / "fonts"
    for font, style in FONT_NAMES:
        pdf.add_font(
            "Open Sans",
            style=style,
            fname=f"{font_path}/{font}",
            uni=True,
        )

    # Page creation
    pdf.add_page()
    pdf.set_font("Open Sans", "B", size=12)
    pdf.cell(
        200,
        10,
        txt=f"News for {term} on {get_date(format=True)}",
        ln=1,
        align="C",
    )

    # News addition
    pdf.set_font("Open Sans", "", size=10)
    for num, (title, link) in enumerate(lines):
        line = f"{num}) {title}\nLink: {link}"
        pdf.multi_cell(0, 10, line, 1, 1)

    # Output
    pdf.output(".".join((filename, "pdf")), "F")


def print_news():
    pass
