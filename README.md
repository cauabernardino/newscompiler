# News Compiler

Compilation of news from a chosen subject for the last 24 hours.

*A project made with the purpose of studying automation with Python.*


###  Remarks for current version:

1) Runs only on Chrome (v84.0.4) for now;
2) Search is regionalized by your current geographic location/language setup.

## Setup

First, clone this repo with:

`git clone https://github.com/cauabernardino/newscompiler`

Then install the requirements with:

`pip install requirements.txt`

And install [Chromedriver](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver) following their instructions.



## Usage

`python newscompiler.py SEARCH_TERM`

The output will be a PDF file with the titles and links to the news.
