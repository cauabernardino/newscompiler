# News Compiler

Compilation of news from a chosen subject for the last 24 hours.


*A project made with the purpose of studying automation, scraping and file manipulation with Python.*

## ⚙️ Setup and usage

- First, clone this repo with: `git clone https://github.com/cauabernardino/newscompiler`
- Enter the directory and install the package:
    ```bash
    $ cd newscompiler
    $ pip install .
    ```
- Usage:
    ```bash
    # With default values to language (english) and time interval (1d)
    $ news "star wars"
    $ news -l en -t 1d "star wars"

    # With  different values
    $ news -l pt -t 7d "star wars"
    ```
    - Use `news -h` or `news --help` for all options
- The output will be a PDF file with news and their links in [TinyURL](https://tinyurl.com/) format.


## 📋 Updates

### 19/02/2022
- Refactor of code to detach functionalities
- Python package configuration
- Time interval choosing
### 17/03/2021
- Total refactor for performance and generalization improvements!
    - Now the script uses `requests` and `lxml.html` for scraping;
    - No more need for Selenium and Chromedriver.
### 22/Oct/2020
- Testing with Chrome v86+, after updating Chromedriver, and working.

### 11/Aug/2020
- Added new command-line option for choosing the language of the search;
- Browser window will run minimized.

### 31/Jul/2020
- First version release.