import pyshorteners
from pdf_gen import pdf_gen
from sys import argv, exit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():

    ## Check if parameters are alright
    if len(argv) != 2:
        print("Usage: python newscompiler.py SEARCH_TERM")
        exit(1)
    
    # Web Scraping
    driver = webdriver.Chrome()
    driver.get('https://news.google.com/')

    searchBox = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]')
    searchBox.send_keys(f"{argv[1]} when:1d")
    searchBox.send_keys(Keys.RETURN)

    s = pyshorteners.Shortener()
    
    try:
        column = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div[2]/div/main/c-wiz/div[1]'))
        )
        pages = column.find_elements_by_class_name("DY5T1d")
    
        news = []

        for page in pages:
            news.append((page.text, s.tinyurl.short(page.get_attribute('href'))))

        pdf_gen(argv[1], news)
            
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
