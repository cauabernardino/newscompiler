import requests
import pyshorteners

from time import time


from newscompiler import SUPPORTED_LANGUAGES
from newscompiler.news import get_news
from newscompiler.parser import arg_parser
from newscompiler.printer import export_pdf


def main():

    # TODO Implement a time context manager
    start = time()

    # Parsing arguments
    parser = arg_parser()
    args = parser.parse_args()
    lang = SUPPORTED_LANGUAGES[args.lang]

    # Getting the news
    search_term = args.search_input
    interval = args.time
    news = get_news(search_term, interval, lang)

    export_pdf(search_term, news)

    end = time()
    print(f"Done in {round(end - start, 2)} seconds! :)")


if __name__ == "__main__":
    main()
