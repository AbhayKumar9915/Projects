from selenium.webdriver.common.by import By
from selenium import webdriver
import time


def Window_Handles():
    driver = webdriver.Chrome()
    driver.get('http://demo.automationtesting.in/Windows.html')
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@class='btn btn-info']").click()
    new_tab_window = driver.window_handles[1]
    driver.switch_to.window(new_tab_window)
    time.sleep(1)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    driver.close()


def New_Separate_Window():
    driver = webdriver.Chrome()
    driver.get('http://demo.automationtesting.in/Windows.html')
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(text(),'Open New Seperate Windows')]").click()
    driver.find_element(By.XPATH, "//button[@class='btn btn-primary']").click()
    new_tab_window = driver.window_handles[1]
    driver.switch_to.window(new_tab_window)
    time.sleep(1)
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.refresh()
    driver.close()


def Separate_Multiple_Window():
    driver = webdriver.Chrome()
    driver.get('http://demo.automationtesting.in/Windows.html')
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(text(),'Open Seperate Multiple Windows')]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "(//button[@class='btn btn-info'])[2]").click()
    new_tab_window = driver.window_handles[2]
    driver.switch_to.window(new_tab_window)
    time.sleep(1)
    driver.close()
    driver.switch_to.window(driver.window_handles[1])
    driver.refresh()
    driver.quit()


Window_Handles()
New_Separate_Window()
Separate_Multiple_Window()
