# from bs4 import element
from selenium import webdriver
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'tab.txt')           # добавляем к этому пути имя файла
print(file_path)


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    element_fname = browser.find_element_by_xpath("//input[@name='firstname']")
    element_fname.send_keys("Имя")

    element_lname = browser.find_element_by_xpath("//input[@name='lastname']")
    element_lname.send_keys("Фамилия")

    element_email = browser.find_element_by_xpath("//input[@name='email']")
    element_email.send_keys("Мой email")
    
    element_upload = browser.find_element_by_xpath("//input[@type='file']")
    element_upload.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
