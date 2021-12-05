import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('iterator', ["236895","236896","236896","236897","236898","236899","236903","236904","236905"])
#@pytest.mark.parametrize('iterator', ["236895"])
def test_guest_should_see_login_link(browser, iterator):
    link = f"https://stepik.org/lesson/{iterator}/step/1"
    browser.get(link)
    browser.implicitly_wait(10)    
    el1 = browser.find_element_by_css_selector('[placeholder="Напишите ваш ответ здесь..."]')
    answer = math.log(int(time.time()))    
    el1.send_keys(str(answer))

    button = browser.find_element_by_css_selector('[class="submit-submission"]')
    button.click()

    ans = browser.find_element_by_css_selector('[class="smart-hints__hint"]')
    ans_text = ans.text
    
    if ans_text != 'Correct!':
        print(ans_text)

    assert ans_text == 'Correct!'