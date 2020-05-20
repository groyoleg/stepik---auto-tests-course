import math
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

def calcSum(x,x1):
    return str(int(num1) + int(num2))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome() #(r'C:\Users\olegg\AppData\Local\Programs\Python\Python37\Selenium\ChromeDriver\chromedriver.exe')
    browser.get(link)

    # questions = browser.find_elements_by_tag_name("span")
    #     #FindElements(By.ClassName("nowrap"))
    # for question in questions:
    #     a = question.text


    element_num1 = browser.find_element_by_id("num1")
    num1 = element_num1.text
    element_num2 = browser.find_element_by_id("num2")
    num2 = element_num2.text

    y = calcSum(num1, num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)
    # print(y)

    button = browser.find_element_by_xpath("//button[@type='submit']").click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
