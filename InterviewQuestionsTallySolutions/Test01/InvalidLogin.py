from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/ABHAY/Selenium/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/login")

driver.find_element_by_id("username").send_keys("tomsmith")
driver.find_element_by_id("password").send_keys("SuperSecretPassword!!")
time.sleep(3)
driver.find_element_by_xpath("//button[@class='radius']").click()
time.sleep(2)

page_title = driver.title
    
assert page_title == "The Internet"

driver.quit()
