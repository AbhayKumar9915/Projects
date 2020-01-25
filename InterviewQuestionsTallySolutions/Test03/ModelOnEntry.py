from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:/Users/ABHAY/Selenium/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/entry_ad")
time.sleep(2)


text = driver.find_element_by_xpath("//div[@class='modal-title']").text

if (text == "THIS IS A MODAL WINDOW"):
    print("Model displayed")
    
else:
    print("Model Not Displayed")

driver.close()
driver.quit()