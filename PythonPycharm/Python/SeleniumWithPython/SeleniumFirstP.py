import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.maximize_window()
driver.get('https://www.google.co.in/')
print(driver.title)
print(driver.current_url)

capText = driver.find_element(By.XPATH, "//a[contains(text(),'Gmail')]").text
driver.find_element(By.NAME, 'q').send_keys(capText)
driver.find_element(By.NAME, 'q').send_keys(Keys.ENTER)

time.sleep(2)
driver.back()
driver.refresh()

# Verifying Test
assert driver.current_url == 'https://www.google.co.in/'
assert driver.title == 'Google'


driver.close()
print('Test Successful')
