import requests
import pyshorteners

from lxml import html
from typing import Iterator, Tuple


def get_news(
    search_term: str, interval: str, lang: str
) -> Iterator[Tuple[str, str]]:
    """Function to scrape Google News and return the searched news.

    Args:
        search_term (str): The term to be searched.
        interval (str): The given interval, allowed in TIME_INTERVALS.
            Defaults to '1d'.
        lang (str): Language to be used, allowed in SUPPORTED_LANGUAGES.
            Defaults to 'en'.

    Returns:
        Generator for the news results, consisting in the news headline and
        its URL in TinyURL format.
    """
    root = "https://news.google.com"
    search_url = f"{root}/search?q={search_term}%20when:{interval}&hl={lang}"

    print(f"Searching for news about {search_term.upper()}...\n")

    source = requests.get(
        search_url,
        cookies={"CONSENT": "YES+42", "User-Agent": "Mozilla/5.0"},
        allow_redirects=True,
    )

    source_html = html.fromstring(source.text)
    elements = source_html.find_class("JtKRv")
    s = pyshorteners.Shortener()

    for element in elements:
        url = f"{root}/{element.getparent().attrib['href']}"
        yield str(element.text_content()), s.tinyurl.short(url)
