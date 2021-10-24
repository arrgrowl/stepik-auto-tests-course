from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)
    get_x = browser.find_element_by_css_selector('[id=input_value]').text
    
    y = calc(get_x)
    
    input = browser.find_element_by_css_selector('[id=answer]')
    input.send_keys(y)

    checkbox = browser.find_element_by_css_selector('[id=robotCheckbox]')
    checkbox.click()

    radio = browser.find_element_by_css_selector('[id=robotsRule]')
    browser.execute_script('return arguments[0].scrollIntoView(true);', radio)
    radio.click()

    button = browser.find_element_by_css_selector('button.btn')
    button.click()



finally:
    time.sleep(10)
    browser.quit()
