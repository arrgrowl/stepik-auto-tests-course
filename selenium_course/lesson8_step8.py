from selenium import webdriver
import os
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = 'file.txt'
file_path = os.path.join(file_name, current_dir)

try:
    browser.get(link)

    firstName = browser.find_element_by_css_selector('[name=firstname]')
    firstName.send_keys('qwe')
    lastName = browser.find_element_by_css_selector('[name=lastname]')
    lastName.send_keys('asd')
    email = browser.find_element_by_css_selector('[name=email]')
    email.send_keys('zxc')

    upload = browser.find_element_by_css_selector('[type=file]')
    upload.send_keys(file_path)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()


finally:
    time.sleep(10)
    browser.quit()
