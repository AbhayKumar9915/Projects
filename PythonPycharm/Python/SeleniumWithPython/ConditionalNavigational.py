import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Navigational Command, back() and forward()
driver = webdriver.Chrome()
driver.get('https://www.facebook.com')
time.sleep(1)
driver.get('https://www.instagram.com')
time.sleep(1)
driver.back()
print(driver.title)
time.sleep(1)
driver.forward()
print(driver.title)
time.sleep(1)

# Conditional Commands is_enabled(), is_displayed(), is_selected()
# Check True and false conditions
driver.get("http://demo.automationtesting.in/Register.html")
ele = driver.find_element(By.XPATH, "//input[@type='text']")
print(ele.is_displayed())
print(ele.is_enabled())

ele = driver.find_element(By.XPATH, "//h1[contains(text(),'Automation Demo Site')]")
print(ele.is_enabled())
print(ele.is_displayed())

radio = driver.find_element(By.XPATH,"//input[@value='Male']")
print(radio.is_selected())
radio.click()
time.sleep(2)
print(radio.is_selected())

driver.quit()
