from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)
    book = browser.find_element_by_id('book')
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    book.click()

    get_x = browser.find_element_by_id('input_value').text
    answer = calc(get_x)

    input = browser.find_element_by_id('answer')
    input.send_keys(answer)

    submit = browser.find_element_by_id('solve')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
