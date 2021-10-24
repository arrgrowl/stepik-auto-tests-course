from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser.get(link)

    value_x = browser.find_element_by_css_selector('[id=treasure]')
    get_x = value_x.get_attribute('valuex')
    print(get_x)
    y = calc(get_x)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    checkbox = browser.find_element_by_css_selector('[id=robotCheckbox]').click()
    radio = browser.find_element_by_css_selector('[id=robotsRule]').click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    time.sleep(10)
    browser.quit()