# Home: добавление комментария
# 1. Откройте http://practice.automationtesting.in/
# 2. Проскролльте страницу вниз на 600 пикселей
# 3. Нажмите на название книги "Selenium Ruby" или на кнопку "READ MORE"
# 4. Нажмите на вкладку "REVIEWS"
# 5. Поставьте 5 звёзд
# 6. Заполните поле "Review" сообщением: "Nice book!"
# 7. Заполните поле "Name"
# 8. Заполните "Email"
# 9. Нажмите на кнопку "SUBMIT"
##################################################################################
from asyncio import sleep
import configparser
import email
import os
from re import search
from select import select
from tabnanny import check
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
##################################################################################
driver = webdriver.Chrome()
driver.implicitly_wait(10)
##################################################################################
driver.get('http://practice.automationtesting.in/')
driver.maximize_window()
##################################################################################
driver.execute_script("window.scrollTo(0,600)")
driver.find_element_by_css_selector("[title='Selenium Ruby']").click()
driver.find_element_by_css_selector("[href='#tab-reviews']").click()
driver.find_element_by_css_selector(".star-5").click()
driver.find_element_by_css_selector("#comment").send_keys("Nice book!")
driver.find_element_by_css_selector("#author").send_keys("Сергей")
driver.find_element_by_css_selector("#email").send_keys("mghallem@gmail.com")
driver.find_element_by_css_selector("#submit").click()
driver.quit() 
