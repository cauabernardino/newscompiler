import pyshorteners
import getopt
from pdf_gen import pdf_gen
from sys import argv, exit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

argv = argv[1:]

def main():

    # Check if parameters are alright
    try:
        opts, args = getopt.getopt(
            argv, 
            'epsf', 
            [
                'english', 
                'portuguese', 
                'spanish', 
                'french'
            ]
        )
        
        if len(args) != 1 or len(opts) > 1:
            print("Usage: python newscompiler.py [language] 'SEARCH_TERM'")
            print("Choose one language: [-e | --english]" 
                "[-p | --portuguese] [-s | --spanish] [-f | --french]")
            exit(1)

    except getopt.GetoptError:
        print("Option not valid!")
        exit(2)

    # Defining language
    lang = 'en' #lang default
    
    for opt, arg in opts:
        if opt in ['-e', '--english']:
            lang = 'en'
        elif opt in ['-p', '--portuguese']:
            lang = 'pt'
        elif opt in ['-s', '--spanish']:
            lang = 'es'
        elif opt in ['-f', '--french']:
            lang = 'fr'

    # Defining driver    
    options = webdriver.ChromeOptions()
    options.add_argument(f'--lang={lang}')
    driver = webdriver.Chrome(options=options)
    driver.minimize_window()
    
    # Web scraping
    driver.get('https://news.google.com/')
    searchBox = driver.find_element_by_xpath(
        '//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]'
        )
    searchBox.send_keys(f"{args[0]} when:1d")
    searchBox.send_keys(Keys.RETURN)

    s = pyshorteners.Shortener()
    
    try:
        column = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((
                By.XPATH, 
                '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div[2]/div/main/c-wiz/div[1]'
                ))
        )
        pages = column.find_elements_by_class_name("DY5T1d")
    
        news = []

        for page in pages:
            news.append((
                page.text, 
                s.tinyurl.short(page.get_attribute('href'))
                ))

        pdf_gen(args[0], news)
            
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
