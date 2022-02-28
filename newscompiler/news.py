import requests
import pyshorteners

from typing import List
from lxml import html


def get_news(search_term: str, interval: str, lang: str) -> List:
    """Function to scrape Google News and return the searched news.

    Args:
        search_term (str): The term to be searched.
        interval (str): The given interval, allowed in TIME_INTERVALS.
            Defaults to '1d'.
        lang (str): Language to be used, allowed in SUPPORTED_LANGUAGES.
            Defaults to 'en'.

    Returns:
        A list of tuples, consisting in the news headline and its URL in
        TinyURL format.
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
    elements = source_html.find_class("DY5T1d RZIKme")

    s = pyshorteners.Shortener()
    news = []

    for element in elements:
        url = f"{root}/{element.attrib['href']}"
        news.append((element.text_content(), s.tinyurl.short(url)))

    return news
