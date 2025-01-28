from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def open_driver(isHeadless: bool) -> webdriver.Chrome:
    options = Options()
    if isHeadless:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    return driver