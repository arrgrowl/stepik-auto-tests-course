from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)

    clickOnButton = browser.find_element_by_css_selector('[type=submit]')
    clickOnButton.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    get_x = browser.find_element_by_css_selector('[id=input_value]').text
    answer = calc(get_x)
    
    input = browser.find_element_by_css_selector('[id=answer]')
    input.send_keys(answer)

    submit = browser.find_element_by_css_selector('[type=submit]')
    submit.click()

finally:
    time.sleep(10)
    browser.quit()