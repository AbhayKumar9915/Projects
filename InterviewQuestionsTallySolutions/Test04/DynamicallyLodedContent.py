from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="C:/Users/ABHAY/Selenium/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/dynamic_loading/1")
time.sleep(2)

driver.find_element_by_xpath("//button[contains(text(),'Start')]").click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h4[contains(text(),'Hello World!')]")))

visible = driver.find_element_by_xpath("//h4[contains(text(),'Hello World!')]").text
time.sleep(2)

print(visible)

driver.quit()