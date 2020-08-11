# News Compiler

Compilation of news from a chosen subject for the last 24 hours.


*A project made with the purpose of studying automation, web scraping and file manipulation with Python.*

Project under [MIT License](https://github.com/cauabernardino/newscompiler/blob/master/LICENSE).


## ☑️ Remarks for current version:

1) Runs only on Chrome (v84.0.4) for now;
2) Command line option for choosing language.

## ⚙️ Setup

First, clone this repo with:

`git clone https://github.com/cauabernardino/newscompiler`

Then install the requirements:
- For Windows: `pip install -r requirements.txt`
- For Debian based Linux distros: `pip3 install -r requirements.txt`

And install [Chromedriver](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver) following their instructions.


## 💻 Usage

Use

* For Windows: `python newscompiler.py [language] 'SEARCH_TERM'`
* For Debian based Linux distros: `python3 newscompiler.py [language] 'SEARCH_TERM'` 

on your terminal, where `SEARCH_TERM` is the subject you want to know about. 

The language options are:

`[-e | --english] [-p | --portuguese] [-s | --spanish] [-f | --french]`

If there is no option, english will be the default value.


Example, if you want to use a subject with more than one word in french, it can be done by:

`python newscompiler.py -f 'star wars'` OR `python newscompiler.py --french 'star wars'` 



The output will be a PDF file with news and their links in [TinyURL](https://tinyurl.com/) format.


## 📋 Updates

### 11/Aug/2020
- Added new command-line option for choosing the language of the search;
- Browser window will run minimized.

### 31/Jul/2020
- First version release.