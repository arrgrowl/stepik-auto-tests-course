from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/find_link_text'
browser = webdriver.Chrome()
word = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    browser.get(link)
    link = browser.find_element_by_link_text(word)
    link.click()
    
    input1 = browser.find_element_by_name('first_name')
    input1.send_keys('Vlad')
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys('Hz')
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys('qwe')
    input4 = browser.find_element_by_id('country')
    input4.send_keys('qwe')
    
    link = browser.find_element_by_class_name('btn')
    link.click()
    time.sleep(15)

finally:
    browser.quit()
