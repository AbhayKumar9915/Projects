from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path="C:/Users/ABHAY/Selenium/chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://the-internet.herokuapp.com/hovers")
time.sleep(2)

action = ActionChains(driver)

element = driver.find_element_by_xpath("//div[@class='example']//div[1]//img[1]")
action.move_to_element(element).perform()
time.sleep(1)
text1 = driver.find_element_by_xpath("//h5[contains(text(),'name: user1')]").text
print(text1)

element1 = driver.find_element_by_xpath("//div[@class='row']//div[2]//img[1]")
action.move_to_element(element1).perform()
time.sleep(1)
text2 = driver.find_element_by_xpath("//h5[contains(text(),'name: user2')]").text
print(text2)

element2 = driver.find_element_by_xpath("//*[@id='content']/div/div[3]/img")
action.move_to_element(element2).perform()
text3 = driver.find_element_by_xpath("//h5[contains(text(),'name: user3')]").text
print(text3)

time.sleep(2)
driver.quit()