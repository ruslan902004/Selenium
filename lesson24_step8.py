from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))

    button1 = browser.find_element_by_css_selector("[id='book']")
    button1.click()

    x_element=browser.find_element_by_id('input_value')
    x=x_element.text
    y=calc(x)

    y_element=browser.find_element_by_id('answer')
    y_element.send_keys(y)

    button=browser.find_element_by_css_selector("[type='submit']")
    button.click()

    # option1 = browser.find_element_by_id('robotCheckbox')
    # option1.click()

    # browser.execute_script("window.scrollBy(0, 500);")

    # option2 = browser.find_element_by_css_selector("[value='robots']")
    # option2.click()

    # browser.execute_script("window.scrollBy(0, 1500);")

    # browser.execute_script('button = document.getElementsByTagName("button")[0];button.scrollIntoView(true);button.click()')
    # button = browser.find_element_by_css_selector("[type='submit']")
    # button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
