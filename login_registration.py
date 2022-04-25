# Registration_login: регистрация аккаунта
# 1. Откройте http://practice.automationtesting.in/
# 2. Нажмите на вкладку "My Account Menu"
# 3. В разделе "Register", введите email для регистрации
# 4. В разделе "Register", введите пароль для регистрации
# • составьте такой пароль, чтобы отобразилось "Medium" или "Strong", иначе регистрация не выполнится
# • почту и пароль сохраните, потребуюутся в дальнейшем
# 5. Нажмите на кнопку "Register"
# Registration_login: логин в систему
# 1. Откройте http://practice.automationtesting.in/
# 2. Нажмите на вкладку "My Account Menu"
# 3. В разделе "Login", введите email для логина # данные можно взять из предыдущего теста
# 4. В разделе "Login", введите пароль для логина # данные можно взять из предыдущего теста
# 5. Нажмите на кнопку "Login"
# 6. Добавьте проверку, что на странице есть элемент "Logout"
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
def registration():
    driver.find_element_by_css_selector("#menu-item-50").click()
    driver.find_element_by_css_selector("#reg_email").send_keys("mghallem@gmail.com")
    driver.find_element_by_css_selector("#reg_password").send_keys("Qwerty123Jhgfdsa$QWERTYasdfg")
    driver.find_element_by_css_selector("[name='register']").click()
    time.sleep(10)
##################################################################################

def login():
    driver.find_element_by_css_selector("#menu-item-50").click()
    driver.find_element_by_css_selector("#username").send_keys("mghallem@gmail.com")
    driver.find_element_by_css_selector("#password").send_keys("Qwerty123Jhgfdsa$QWERTYasdfg")
    driver.find_element_by_css_selector("[name='login']").click()
    time.sleep(10)
    result = driver.find_element_by_xpath("//a[contains(text(), 'Logout')]").text == "Logout"
    print(result)

login()

driver.quit()
