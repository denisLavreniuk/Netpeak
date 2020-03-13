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
    
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='btn green-btn']")))
    finally:
        browser.find_element_by_xpath("//a[@class='btn green-btn']").click()
    try:
        WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='upload']")))
    finally:
        sendFile=browser.find_element_by_xpath("//input[@name='up_file']")
        sendFile.send_keys("C:\\git\\Netpeak\\Netpeak\\Netpeak.png")
    try:
        browser.find_element_by_xpath("//div[@id='up_file_name']//label[@class='control-label'][contains(text(),'(')]")
    finally:
        try:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='inputName']")))
        finally:
            name=browser.find_element_by_xpath("//input[@id='inputName']")
            name.send_keys(''.join(random.choice(string.ascii_letters) for i in range(10)))
        
        try:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='inputLastname']")))
        finally:
            name=browser.find_element_by_xpath("//input[@id='inputLastname']")
            name.send_keys(''.join(random.choice(string.ascii_letters) for i in range(10)))
        try:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='inputEmail']")))
        finally:
            name=browser.find_element_by_xpath("//input[@id='inputEmail']")
            name.send_keys(''.join(random.choice(string.ascii_letters) for i in range(10))+'@'+''.join(random.choice(string.ascii_letters) for i in range(5))+'.com')
            browser.find_element_by_xpath("//button[@id='submit']").click()






        


def main():
    WorkInNetpeak()
    



if __name__ == '__main__':
    main()