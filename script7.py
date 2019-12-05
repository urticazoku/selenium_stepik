from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
browser.find_element_by_id("book").click()
x=int(browser.find_element_by_id("input_value").text)
answer = str(math.log(abs(12*math.sin(x))))
input1=browser.find_element_by_id("answer")
input1.send_keys(answer)
browser.find_element_by_id("solve").click()
assert True

