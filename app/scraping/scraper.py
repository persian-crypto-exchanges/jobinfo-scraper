from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from app.scraping.config import open_driver


def scap_wallex():
    url = "https://wallex.ir/landing/career/"
    driver = open_driver(False)
    
    try:
        driver.get(url)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='combobox']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":Rilcrald56:"]/li[2]'))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='combobox' and normalize-space()='همه واحدها']"))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id=":Rildbald56:"]/li[2]'))).click()

        page_source = driver.page_source
        soup = BeautifulSoup(page_source, "html.parser")
        return soup.prettify()
    
    finally:
        driver.quit()