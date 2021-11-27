from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id('num1')
    #x = x_element.get_attribute('valuex')
    x = int(x_element.text)
    y_element = browser.find_element_by_id('num2')
    #x = x_element.get_attribute('valuex')
    y = int(y_element.text)

    z = x + y
    
    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_value(str(z))
    
    # y_element = browser.find_element_by_id('answer')
    # y_element.send_keys(y)

    # option1 = browser.find_element_by_id('robotCheckbox')
    # option1.click()

    # option2 = browser.find_element_by_css_selector("[value='robots']")
    # option2.click()

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла