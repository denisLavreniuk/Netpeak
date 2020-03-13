import random
import string
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

browser = webdriver.Chrome()
browser.get('https://netpeak.ua/')
browser.wait = WebDriverWait(browser, 5)


def WorkInNetpeak():
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "*//li[@class='blog']//a")))
    finally:
        browser.find_element_by_xpath("//li[@class='blog']//a").click()


def main():
    WorkInNetpeak()
    



if __name__ == '__main__':
    main()