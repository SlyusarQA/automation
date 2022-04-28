

##################################################################################
from asyncio import sleep
from cgitb import text
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
def login():
    driver.find_element_by_css_selector("#menu-item-50").click()
    driver.find_element_by_css_selector("#username").send_keys("mghallem@gmail.com")
    driver.find_element_by_css_selector("#password").send_keys("Qwerty123Jhgfdsa$QWERTYasdfg")
    driver.find_element_by_css_selector("[name='login']").click()
    time.sleep(10)
##################################    
""" Shop: отображение страницы товара
1. Откройте http://practice.automationtesting.in/
2. Залогиньтесь
3. Нажмите на вкладку "Shop"
4. Откройте книгу "HTML 5 Forms"
5. Добавьте тест, что заголовок книги назвается: "HTML5 Forms" """
def shop1():
    login()
    driver.find_element_by_xpath("//a [contains(text(), 'Shop')]").click()
    driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']").click()
    result = driver.find_element_by_css_selector("[itemprop='name']").text == "HTML5 Forms"
    print(result)
    driver.quit()
""" Shop: количество товаров в категории
1. Откройте http://practice.automationtesting.in/
2. Залогиньтесь
3. Нажмите на вкладку "Shop"
4. Откройте категорию "HTML"
5. Добавьте тест, что отображается три товара """
def shop2():
    login()
    driver.find_element_by_xpath("//a [contains(text(), 'Shop')]").click()
    driver.find_element_by_xpath("//a [contains(text(), 'HTML')]").click()
    result = len(driver.find_elements_by_css_selector("ul >li.product"))
    print(f"Товаров на странице {result}")
""" Shop: сортировка товаров
1. Откройте http://practice.automationtesting.in/
2. Залогиньтесь
3. Нажмите на вкладку "Shop"
4. Добавьте тест, что в селекторе выбран вариант сортировки по умолчанию
• Используйте проверку по value
5. Отсортируйте товары по цене от большей к меньшей
• в селекторах используйте класс Select
6. Снова объявите переменную с локатором основного селектора сортировки # т.к после сортировки страница обновится
7. Добавьте тест, что в селекторе выбран вариант сортировки по цене от большей к меньшей
• Используйте проверку по value """
def shop3():
    login()
    driver.find_element_by_xpath("//a [contains(text(), 'Shop')]").click()
    text_default = driver.find_element_by_css_selector("[name='orderby'] > option[value='menu_order']").text
    if driver.find_element_by_css_selector("[name='orderby'] > option[value='menu_order']").get_attribute("selected"): print(f"Сортировка по {text_default} ")
    else: print(f"Сортировка не {text_default}")
    driver.find_element_by_css_selector("[name='orderby'] > option[value='price-desc']").click()
    time.sleep(5)
    text_high_low = driver.find_element_by_css_selector("[name='orderby'] > option[value='price-desc']").text
    if driver.find_element_by_css_selector("[name='orderby'] > option[value='price-desc']").get_attribute("selected"): print(f"Сортировка по {text_high_low} ")
    else: print(f"Сортировка не {text_high_low}")
""" Shop: отображение, скидка товара
1. Откройте http://practice.automationtesting.in/
2. Залогиньтесь
3. Нажмите на вкладку "Shop"
4. Откройте книгу "Android Quick Start Guide"
5. Добавьте тест, что содержимое старой цены = "₹600.00" # используйте assert
6. Добавьте тест, что содержимое новой цены = "₹450.00" # используйте assert
7. Добавьте явное ожидание и нажмите на обложку книги
• Подберите такой селектор и тайминги, чтобы открылось окно предпросмотра картинки (не вся картинка на всю страницу)
8. Добавьте явное ожидание и закройте предпросмотр нажав на крестик (кнопка вверху справа) """
def shop4():
    login()
    driver.find_element_by_xpath("//a [contains(text(), 'Shop')]").click()
    driver.find_element_by_css_selector("[title='Android Quick Start Guide']").click()
    assert driver.find_element_by_css_selector("del>span").text == "₹600.00"
    assert driver.find_element_by_css_selector("ins>span").text == "₹450.00"
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[title='Android Quick Start Guide']"))).click()
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"[class='pp_close']"))).click()
    time.sleep(3)
""" Shop: проверка цены в корзине
1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
2. Нажмите на вкладку "Shop"
3. Добавьте в корзину книгу "HTML5 WebApp Development" # см. комментарии в самом низу
4. Добавьте тест, что возле коризны(вверху справа) количество товаров = "1 item", а стоимость = "₹180.00"
• Используйте для проверки assert
5. Перейдите в корзину
6. Используя явное ожидание, проверьте что в Subtotal отобразилась стоимость
7. Используя явное ожидание, проверьте что в Total отобразилась стоимость """
def shop5():
    driver.find_element_by_xpath("//a [contains(text(), 'Shop')]").click()
    driver.find_element_by_css_selector("[data-product_id='182']").click()
    time.sleep(5)
    result1 = driver.find_element_by_css_selector("[class='cartcontents']").text
    time.sleep(5)
    assert result1 == "1 Item"
    result2 = driver.find_element_by_css_selector("[class='amount']").text 
    time.sleep(5)
    assert result2 == "₹180.00"
    driver.find_element_by_css_selector("[class='cartcontents']").click()
    time.sleep(5)
    WebDriverWait(driver,20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[data-title='Subtotal']> span"),result2))
    time.sleep(5)
    WebDriverWait(driver,20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"[class='product-subtotal'] > span"),result2))
""" Shop: работа в корзине
Иногда, даже явные ожидания не помогают избежать ошибки при нахождении элемента, этот сценарий один из таких, используйте time.sleep()
1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
2. Нажмите на вкладку "Shop"
3. Добавьте в корзину книги "HTML5 WebApp Development" и "JS Data Structures and Algorithm"
• Перед добавлением первой книги, проскролльте вниз на 300 пикселей
• После добавления 1-й книги добавьте sleep
4. Перейдите в корзину
5. Удалите первую книгу
• Перед удалением добавьте sleep
6. Нажмите на Undo (отмена удаления)
7. В Quantity увеличьте количесто товара до 3 шт для "JS Data Structures and Algorithm“
• Предварительно очистите поле с помощью локатор_поля.clear()
8. Нажмите на кнопку "UPDATE BASKET"
9. Добавьте тест, что value элемента quantity для "JS Data Structures and Algorithm" равно 3 # используйте assert
10. Нажмите на кнопку "APPLY COUPON"
• Перед нажатимем добавьте sleep
11. Добавьте тест, что возникло сообщение: "Please enter a coupon code."
# если эти книги будут out of stock - тогда вместо них добавьте книгу HTML5 Forms и любую доступную книгу по JS и выполните тесты по аналогии """
def shop6():
    driver.find_element_by_xpath("//a [contains(text(), 'Shop')]").click()
    driver.execute_script("window.scrollTo(0,600)")
    driver.find_element_by_css_selector("[data-product_id='182']").click()
    time.sleep(3)
    driver.find_element_by_css_selector("[data-product_id='180']").click()
    time.sleep(3)
    driver.find_element_by_css_selector("[class='cartcontents']").click()
    time.sleep(3)
    driver.find_element_by_css_selector("[data-product_id='182']").click()
    time.sleep(3)
    driver.find_element_by_css_selector(".woocommerce-message >a").click()
    time.sleep(3)
    driver.find_element_by_css_selector(".quantity >input:nth-child(1)").clear() # чистим поле
    time.sleep(3)
    driver.find_element_by_css_selector(".quantity >input:nth-child(1)").send_keys("3")
    time.sleep(3)
    driver.find_element_by_css_selector("[value='Update Basket']").click()
    time.sleep(3)
    assert driver.find_element_by_css_selector(".quantity >input:nth-child(1)").get_attribute("value") == "3"
    time.sleep(3)
    driver.find_element_by_css_selector("[value='Apply Coupon']").click()
    time.sleep(3)
    assert driver.find_element_by_css_selector(".woocommerce >ul>li").text == "Please enter a coupon code."


""" Shop: покупка товара
1. Откройте http://practice.automationtesting.in/ # в этом тесте логиниться не нужно
2. Нажмите на вкладку "Shop" и проскролльте на 300 пикселей вниз
3. Добавьте в корзину книгу "HTML5 WebApp Development"
4. Перейдите в корзину
5. Нажмите "PROCEED TO CHECKOUT"
• Перед нажатием, добавьте явное ожидание
6. Заполните все обязательные поля
• Перед заполнением first name, добавьте явное ожидание
• Для заполнения country нужно: нажать на селектор - > ввести название в поле ввода - > нажать на вариант который отобразится ниже ввода
• Чтобы выбрать селектор нижний вариант после ввода, используйте кнопку нажмите на неё, затем на вариант в списке ниже
7. Выберите способ оплаты "Check Payments"
• Перед выбором, проскролльте на 600 пикселей вниз и добавьте sleep
8. Нажмите PLACE ORDER
9. Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
10. Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments" """
def shop7():
    driver.find_element_by_xpath("//a [contains(text(), 'Shop')]").click()
    driver.execute_script("window.scrollTo(0,300)")
    driver.find_element_by_css_selector("[data-product_id='182']").click()
    time.sleep(3)
    driver.find_element_by_css_selector("[class='cartcontents']").click()
    time.sleep(3)
    driver.find_element_by_css_selector(".wc-proceed-to-checkout >a").click()
    driver.find_element_by_id("billing_first_name").send_keys("Sergey")
    driver.find_element_by_id("billing_last_name").send_keys("Slyusar")
    driver.find_element_by_id("billing_email").send_keys("mail@mail.ru")
    driver.find_element_by_id("billing_phone").send_keys("89995557799")
    driver.find_element_by_css_selector("span>[role='presentation']").click()
    time.sleep(2)
    driver.find_element_by_id("s2id_autogen1_search").send_keys("Russia")
    time.sleep(2)
    driver.find_element_by_css_selector("span.select2-match").click()
    time.sleep(2)
    driver.find_element_by_id("billing_address_1").send_keys("Lenin str. 22")
    driver.find_element_by_id("billing_state").send_keys("Moscow")
    driver.find_element_by_id("billing_city").send_keys("Moscow")
    driver.find_element_by_id("billing_postcode").send_keys("662640")
    driver.execute_script("window.scrollTo(0,600)")
    time.sleep(5)
    driver.find_element_by_id("payment_method_cheque").click()
    time.sleep(2)
    driver.find_element_by_id("place_order").click()
    time.sleep(5)
    assert WebDriverWait(driver,30).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"div>.woocommerce-thankyou-order-received"),"Thank you. Your order has been received.")) == True
    assert WebDriverWait(driver,30).until(EC.text_to_be_present_in_element((By.XPATH,"//tfoot/tr[3]/td"),"Check Payments")) == True
#shop1()
#shop2()
#shop3()
#shop4()
#shop5()
#shop6()
#shop7()


driver.quit()