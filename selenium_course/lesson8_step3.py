from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()

def sum(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return str(num1 + num2)

try:
    browser.get(link)
    
    get_num1 = browser.find_element_by_css_selector('[id=num1]').text
    get_num2 = browser.find_element_by_css_selector('[id=num2]').text
    answer = sum(get_num1, get_num2)

    select = Select(browser.find_element_by_tag_name('select'))
    select.select_by_value(answer)

    submit = browser.find_element_by_css_selector('button.btn').click()

finally:
    time.sleep(10)
    browser.quit()
