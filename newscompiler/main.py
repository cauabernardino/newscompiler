from newscompiler import SUPPORTED_LANGUAGES, arg_parser
from newscompiler.news import get_news
from newscompiler.printer import export_pdf, print_news
from newscompiler.tools import TimeContext


def main():
    """Entry-point for News Compiler."""
    parser = arg_parser()
    args = parser.parse_args()

    with TimeContext() as total_time:
        # Getting the news
        lang = SUPPORTED_LANGUAGES[args.lang]
        search_term = args.search_input
        interval = args.time

        news = get_news(search_term, interval, lang)

        if args.pdf:
            export_pdf(search_term, news)
            return
        print_news(search_term, news)

    print(total_time)


if __name__ == "__main__":
    main()
