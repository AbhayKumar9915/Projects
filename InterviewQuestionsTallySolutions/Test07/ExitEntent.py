from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:/Users/ABHAY/Selenium/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/exit_intent")
time.sleep(2)

action = ActionChains(driver)

element = driver.find_element_by_xpath("//h3[contains(text(),'Exit Intent')]")
action.move_to_element(element).perform()

time.sleep(5)
driver.close()
driver.quit()