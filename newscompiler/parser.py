from argparse import ArgumentParser

from newscompiler import SUPPORTED_LANGUAGES, TIME_INTERVALS


def arg_parser() -> ArgumentParser:
    """Wrapper function for the argument parser."""

    parser = ArgumentParser(description="Compiler of news for given subject.")

    parser.add_argument(
        "search_input", help="input term to be searched", action="store"
    )
    parser.add_argument(
        "-l",
        "--lang",
        help="choose search language",
        default="en",
        choices=SUPPORTED_LANGUAGES.keys(),
    )
    parser.add_argument(
        "-t",
        "--time",
        help="choose time interval for the search",
        default="1d",
        choices=TIME_INTERVALS,
    )
    parser.add_argument(
        "-p",
        "--pdf",
        help="export the results to pdf",
        action="store_true",
        default=False,
    )

    return parser
