import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC



def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome() #(r'C:\Users\olegg\AppData\Local\Programs\Python\Python37\Selenium\ChromeDriver\chromedriver.exe')
    # browser.implicitly_wait(11)
    browser.get(link)

    # price= browser.find_element_by_id("prise").text

    WebDriverWait(browser,11).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element_by_xpath("//button[@id='book']").click()



    # new_window = browser.window_handles[1]
    # browser.switch_to.window(new_window)
    # confirm = browser.switch_to.alert
    # confirm.accept()

    element_num1 = browser.find_element_by_id("input_value")
    num1 = element_num1.text
    y=calc(num1)

    answer = browser.find_element_by_id("answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    # time.sleep(1)

    button = browser.find_element_by_xpath("//button[@type='submit']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
