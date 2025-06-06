from selenium import webdriver
from selenium.webdriver.common.by import By
from PIL import Image

driver = webdriver.Chrome()
driver.get("https://google.com")
driver.maximize_window()
driver.find_element(By.NAME,'q').send_keys('Test')
driver.save_screenshot('Google.png')
ss=Image.open('Google.png')
ss.show()
driver.quit()