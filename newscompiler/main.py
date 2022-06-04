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

        news = get_news(args.search_input, args.time, lang)

        if args.pdf:
            export_pdf(args.search_input, list(news))
        else:
            print_news(args.search_input, news)

    print(total_time)


if __name__ == "__main__":
    main()
