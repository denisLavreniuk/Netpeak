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
            inputLastname=browser.find_element_by_xpath("//input[@id='inputLastname']")
            inputLastname.send_keys(''.join(random.choice(string.ascii_letters) for i in range(10)))
        try:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='inputEmail']")))
        finally:
            inputEmail=browser.find_element_by_xpath("//input[@id='inputEmail']")
            inputEmail.send_keys(''.join(random.choice(string.ascii_letters) for i in range(10))+'@'+''.join(random.choice(string.ascii_letters) for i in range(5))+'.com')
        try:
            WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='inputLastname']")))
        finally:
            browser.find_element_by_xpath("//select[@name='bd']").click()#день рождения
            try:
              WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='bd']//option[contains(text(),'19')]")))  
            finally:
                browser.find_element_by_xpath("//select[@name='bd']//option[contains(text(),'19')]").click()

            browser.find_element_by_xpath("//select[@name='bm']").click()#месяц рождения
            try:
              WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@name='bm']//option[2]")))  
            finally:
                browser.find_element_by_xpath("//select[@name='bm']//option[2]").click()

            browser.find_element_by_xpath("//select[@name='by']").click()#год рождения
            try:
              WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//option[contains(text(),'1999')]")))  
            finally:
                browser.find_element_by_xpath("//option[contains(text(),'1999')]").click()

            try:#номер телефона
                WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@id='inputPhone']")))
            finally:
                inputLastname=browser.find_element_by_xpath("//input[@id='inputPhone']")
                inputLastname.send_keys(''.join(random.choice(string.digits) for i in range(10)))
        browser.find_element_by_xpath("//button[@id='submit']").click()
        browser.find_element_by_xpath("//div[@class='logo-block']//a//img").click()
        if browser.current_url=="https://netpeak.ua/":
            print("=====================================================================")
            print("all correct")
            print("=====================================================================")

def main():
    WorkInNetpeak()

if __name__ == '__main__':
    main()