from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/ABHAY/Selenium/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/broken_images")
time.sleep(2)


Links = driver.find_elements_by_tag_name("img")
for i in Links:
    print(i)

driver.quit()
