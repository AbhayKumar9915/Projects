from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/ABHAY/Selenium/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/dynamic_loading/1")
time.sleep(2)

driver.find_element_by_xpath("//button[contains(text(),'Start')]").click()

time.sleep(5)
visible = driver.find_element_by_xpath("//h4[contains(text(),'Hello World!')]")
visible.is_displayed()
driver.close()
driver.quit()