import pyshorteners
from sys import argv, exit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    
    driver = webdriver.Chrome()
    driver.get('https://news.google.com/')
    print(driver.title)

    searchBox = driver.find_element_by_xpath('//*[@id="gb"]/div[2]/div[2]/div/form/div[1]/div/div/div/div/div[1]/input[2]')
    searchBox.send_keys("aviação")
    searchBox.send_keys(Keys.RETURN)

    s = pyshorteners.Shortener()

    try:
        column = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div[2]/div/main/c-wiz/div[1]'))
        )
        pages = column.find_elements_by_class_name("DY5T1d")
        count = 0

        for page in pages:
            count += 1
            print(f"{count}) {page.text} | {s.tinyurl.short(page.get_attribute('href'))}")
            
    finally:
        driver.quit()


if __name__ == "__main__":
    main()

