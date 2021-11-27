from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'input.txt')           # добавляем к этому пути имя файла 


try:
    browser = webdriver.Chrome()
    browser.get(link)

    ima = browser.find_element_by_css_selector('[placeholder="Enter first name"]')
    ima.send_keys('Vasia')

    fam = browser.find_element_by_css_selector('[placeholder="Enter last name"]')
    fam.send_keys('Petrov')

    em = browser.find_element_by_css_selector('[placeholder="Enter email"]')
    em.send_keys('ya@ya.com')

    inFileInput = browser.find_element_by_css_selector('[id="file"]')
    inFileInput.send_keys(file_path)

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()


    # y_element = browser.find_element_by_id('answer')
    # y_element.send_keys(y)

    # option1 = browser.find_element_by_id('robotCheckbox')
    # option1.click()

    # browser.execute_script("window.scrollBy(0, 500);")

    # option2 = browser.find_element_by_css_selector("[value='robots']")
    # option2.click()

    # browser.execute_script("window.scrollBy(0, 1500);")

    # browser.execute_script('button = document.getElementsByTagName("button")[0];button.scrollIntoView(true);button.click()')
    # #button = browser.find_element_by_css_selector("[type='submit']")
    # #button.click()
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла