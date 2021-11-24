from selenium import webdriver
import time 

link = " http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath('//body/div/form/div/div/input [@class="form-control first"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//body/div/form/div/div/input [@class="form-control second"]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//body/div/form/div/div/input [@class="form-control third"]')
    input3.send_keys("Smolensk@Smolensk.ru")
    input4 = browser.find_element_by_xpath('//body/div/form/div/div/input [@placeholder="Input your phone:"]')
    input4.send_keys("99999999999999999")
    input5 = browser.find_element_by_xpath('//body/div/form/div/div/input [@placeholder="Input your address:"]')
    input5.send_keys("Russia Oren")
    button = browser.find_element_by_xpath('//body/div/form/button')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла