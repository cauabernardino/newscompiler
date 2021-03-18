import requests
import getopt
import pyshorteners
from time import time
from pdf_gen import pdf_gen
from sys import argv, exit
from lxml import html

argv = argv[1:]

def main():

    # Check if parameters are alright
    try:
        opts, args = getopt.getopt(
            argv, 
            'epsf', 
            [
                'english', 
                'portuguese', 
                'spanish', 
                'french'
            ]
        )
        
        if len(args) != 1 or len(opts) > 1:
            print("Usage: python newscompiler.py [language] 'SEARCH_TERM'")
            print("Choose one language: [-e | --english]" 
                "[-p | --portuguese] [-s | --spanish] [-f | --french]")
            exit(1)

    except getopt.GetoptError:
        print("Option not valid!")
        exit(2)

    # Defining language
    lang = 'en-US' #lang default
    
    for opt, arg in opts:
        if opt in ['-e', '--english']:
            lang = 'en-US'
        elif opt in ['-p', '--portuguese']:
            lang = 'pt-BR'
        elif opt in ['-s', '--spanish']:
            lang = 'es-419'
        elif opt in ['-f', '--french']:
            lang = 'fr'

    # Scraping
    root = "https://news.google.com"
    search_term = args[0]
    search_url = f"{root}/search?q='{search_term} when:1d'&hl={lang}"

    print(f"Searching for news about {search_term.upper()}")
    source = requests.get(search_url)

    source_html = html.fromstring(source.text)
    elements = source_html.find_class("DY5T1d RZIKme")

    # Format and generate PDF
    s = pyshorteners.Shortener()
    news = []

    print("Generating PDF...")

    for element in elements:
        url = f"{root}/{element.attrib['href']}"
        news.append((
            element.text_content(),
            s.tinyurl.short(url)
        ))

    pdf_gen(search_term, news)


if __name__ == "__main__":
    start = time()
    main()
    end = time()

    print(f"Done in {round(end - start, 2)} seconds! :)")
