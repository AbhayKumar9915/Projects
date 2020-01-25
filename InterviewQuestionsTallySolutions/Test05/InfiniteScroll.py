from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/ABHAY/Selenium/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/infinite_scroll")
time.sleep(2)


driver.execute_script("window.scrollTo(0, 1080)")
time.sleep(3)
driver.execute_script("window.scrollTo(0, 1080)")
time.sleep(3)
driver.execute_script("window.scrollTo(0, 1080)")
time.sleep(3)
driver.execute_script("window.scrollTo(0, 1080)")
time.sleep(3)
driver.close()
driver.quit()