from selenium.webdriver.common.by import By
from selenium import webdriver
import time


def SingleFrame():
    driver = webdriver.Chrome()
    driver.get('http://demo.automationtesting.in/Frames.html')
    frame_id = 'singleframe'
    driver.switch_to.frame(driver.find_element(By.ID, frame_id))
    # driver.switch_to.frame(0) #switch with index
    driver.find_element(By.XPATH,"//input[@type='text']").send_keys('Single Frame')
    time.sleep(3)
    driver.close()


def MultipleFrame():
    driver = webdriver.Chrome()
    driver.get('http://demo.automationtesting.in/Frames.html')
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[contains(text(),'Iframe with in an Iframe')]").click()
    time.sleep(1)
    frame_xpath = "//iframe[@src='MultipleFrames.html']"
    driver.switch_to.frame(driver.find_element(By.XPATH,frame_xpath))
    sec_frame = "/html/body/section/div/div/iframe"
    driver.switch_to.frame(driver.find_element(By.XPATH,sec_frame))
    driver.find_element(By.XPATH,"//input[@type='text']").send_keys('Multiple Frame')
    time.sleep(2)
    driver.close()


SingleFrame()
MultipleFrame()
