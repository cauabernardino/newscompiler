# News Compiler

Compilation of news from a chosen subject for the last 24 hours.

*A project made with the purpose of studying automation with Python.*


###  Remarks for current version:

1) Runs only on Chrome (v84.0.4) for now;
2) Search is regionalized by your current geographic location/language setup.

## Setup

First, clone this repo with:

`git clone https://github.com/cauabernardino/newscompiler`

Then install the requirements:
- For Windows: `pip install -r requirements.txt`
- For Debian based Linux distros: `pip3 install -r requirements.txt`

And install [Chromedriver](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver) following their instructions.



## Usage

Use

* For Windows: `python newscompiler.py SEARCH_TERM`
* For Debian based Linux distros: `python3 newscompiler.py SEARCH_TERM` 

on your terminal, where `SEARCH_TERM` is the subject you want to know about. 

If you want to use a subject with more than one word, it can be done using quotes as the example below:

`python newscompiler.py 'star wars'`



The output will be a PDF file with news and their links in [TinyURL](https://tinyurl.com/) format.
