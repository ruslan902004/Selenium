from selenium import webdriver
import time
import os 

browser = webdriver.Chrome()
link = "https://suninjuly.github.io/execute_script.html"
browser.get(link)

button = browser.find_element_by_tag_name("button")

browser.execute_script('button = document.getElementsByTagName("button")[0];button.scrollIntoView(true);button.click()')
#browser.execute_script("window.scrollBy(0, 1000);")
#button.click()

time.sleep(10)
browser.quit()