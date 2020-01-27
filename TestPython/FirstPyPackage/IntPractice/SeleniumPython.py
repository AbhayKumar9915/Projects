from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\ABHAY\\Selenium\\chromedriver.exe")
driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
#time.sleep(3)
driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
time.sleep(2)
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
time.sleep(2)
driver.find_element_by_xpath("//input[@id='btnLogin']").click()
time.sleep(2)
driver.quit()
