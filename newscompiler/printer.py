from pathlib import Path
from fpdf import FPDF
from typing import Generator, List

from newscompiler.tools import get_date


FONT_NAMES = (
    ("OpenSans-Regular.ttf", ""),
    ("OpenSans-Bold.ttf", "B"),
    ("OpenSans-Italic.ttf", "I"),
    ("OpenSans-BoldItalic.ttf", "BI"),
)


def export_pdf(search_term: str, lines: List) -> FPDF:
    """Handles the creation and exporting of news list into a PDF file.

    Args:
        search_term (str): The term that was searched.
        lines (List[Tuple[str, str]]): List of tuples with

    Returns:
        A PDF file in the package root directory.
    """
    filename = " ".join((get_date(), search_term.upper()))

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
        txt=f"News for {search_term.upper()} on {get_date(format=True)}",
        ln=1,
        align="C",
    )

    # News addition
    pdf.set_font("Open Sans", "", size=10)
    for num, (title, link) in enumerate(lines):
        line = f"{num + 1}) {title}\nLink: {link}"
        pdf.multi_cell(0, 10, line, 1, 1)

    # Output
    return pdf.output(".".join((filename, "pdf")), "F")


def print_news(search_term: str, news: Generator) -> None:
    """Prints the news to the console.

    Args:
        search_term (str): The term that was searched.
        lines (List[Tuple[str, str]]): List of tuples with
    """
    headline = f"News for {search_term.upper()} on {get_date(format=True)}"
    print(headline)

    for num, (title, link) in enumerate(news):
        print("----------------------------------------")
        line = f"{num + 1}) {title}\n{link}"
        print(line)
    print("\n")
