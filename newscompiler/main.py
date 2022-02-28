from newscompiler import SUPPORTED_LANGUAGES

from newscompiler.news import get_news
from newscompiler.parser import arg_parser
from newscompiler.printer import export_pdf
from newscompiler.tools import TimeContext


def main():

    # Parsing arguments
    parser = arg_parser()
    args = parser.parse_args()

    with TimeContext(True):
        # Getting the news
        lang = SUPPORTED_LANGUAGES[args.lang]
        search_term = args.search_input
        interval = args.time

        news = get_news(search_term, interval, lang)
        export_pdf(search_term, news)


if __name__ == "__main__":
    main()
