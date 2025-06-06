import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

def MouseHover():
    driver.get('http://demo.automationtesting.in/AutoComplete.html')
    time.sleep(2)
    driver.find_element(By.ID,"searchbox").send_keys('a')
    time.sleep(1)
    first_hover_xpath = driver.find_element(By.XPATH,"//a[contains(text(),'Angola')]")
    hover = ActionChains(driver).move_to_element(first_hover_xpath)
    hover.perform()
    time.sleep(1)
    sec_hover = driver.find_element(By.XPATH,"//a[contains(text(),'Albania')]")
    hover1 = ActionChains(driver).move_to_element(sec_hover)
    hover1.perform()
    time.sleep(2)
    third_hover = driver.find_element(By.XPATH,"//a[contains(text(),'Argentina')]")
    Action = ActionChains(driver).move_to_element(third_hover)
    time.sleep(1)
    Action.click()
    Action.perform()
    time.sleep(2)
    driver.close()


def MouseHover02():
    driver.get('https://rahulshettyacademy.com/AutomationPractice/')
    time.sleep(2)
    driver.execute_script('window.scrollTo(0,1080)')
    hover = driver.find_element(By.ID,"mousehover")
    ActionChains(driver).move_to_element(hover).perform()
    time.sleep(1)
    sec_xpath = driver.find_element(By.XPATH,"//a[contains(text(),'Top')]")
    sec_xpath.click()
    time.sleep(2)
    driver.close()


MouseHover()
#MouseHover02()
