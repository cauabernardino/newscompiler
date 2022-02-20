from argparse import ArgumentParser

from newscompiler import SUPPORTED_LANGUAGES


def arg_parser() -> ArgumentParser:
    """Wrapper function for the argument parser."""

    parser = ArgumentParser(
        description="Compiler of news from given subject."
    )

    parser.add_argument(
        "term", action="store"
    )
    parser.add_argument(
        "-l",
        "--lang",
        help="choose search language",
        default="english",
        choices=SUPPORTED_LANGUAGES
    )

    return parser
