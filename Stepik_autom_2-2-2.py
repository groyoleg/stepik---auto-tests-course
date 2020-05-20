import math
import time

from selenium.webdriver.support.ui import Select
from selenium import webdriver


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# def calcSum(x,x1):
#     return str(int(num1) + int(num2))

try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome() #(r'C:\Users\olegg\AppData\Local\Programs\Python\Python37\Selenium\ChromeDriver\chromedriver.exe')
    browser.get(link)

    # questions = browser.find_elements_by_tag_name("span")
    #     #FindElements(By.ClassName("nowrap"))
    # for question in questions:
    #     a = question.text


    element_num1 = browser.find_element_by_id("input_value")
    num1 = element_num1.text
    y=calc(num1)

    answer = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    # time.sleep(1)

    element_Chbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element_Chbox)
    element_Chbox.click()
    # time.sleep(1)

    element_Rbox = browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", element_Rbox)
    element_Rbox.click()
    # time.sleep(1)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
