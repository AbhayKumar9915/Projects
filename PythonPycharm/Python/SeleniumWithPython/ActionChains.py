import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")

#Mouse Hover
element = driver.find_element(By.XPATH,"//button[@class='dropbtn']")
driver.execute_script("window.scrollTo(0, 1100)")
ActionChains(driver).move_to_element(to_element=element).perform()
time.sleep(2)

#Double Click
driver.execute_script("window.scrollTo(0, 1200)")
double_click_btn=driver.find_element(By.XPATH,"//button[contains(text(),'Copy Text')]")
ActionChains(driver).double_click(double_click_btn).perform()
time.sleep(2)

#Drag and Drop
driver.execute_script("window.scrollTo(0, 1400)")
source_ele=driver.find_element(By.ID,"draggable")
target_ele=driver.find_element(By.ID,"droppable")
ActionChains(driver).drag_and_drop(source=source_ele,target=target_ele).perform()
time.sleep(2)

#Slider - Click and Hold
driver.execute_script("window.scrollTo(0, 1700)")
element_to_hold = driver.find_element(By.XPATH,"(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[2]")
ActionChains(driver).click_and_hold(element_to_hold).move_by_offset(100,0).perform()
time.sleep(2)

#Scroll Up/Down
ActionChains(driver).scroll_by_amount(0,-1000).perform()
time.sleep(2)
ActionChains(driver).scroll_by_amount(0,1000).perform()
time.sleep(2)

driver.close()