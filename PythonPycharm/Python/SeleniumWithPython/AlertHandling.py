from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium import webdriver
import time


def alert_accept():
    driver = webdriver.Chrome()
    driver.get('http://demo.automationtesting.in/Alerts.html')
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[contains(text(),'alert box:')]").click()
    time.sleep(1)
    # with alert class
    Alert(driver).accept()
    driver.refresh()
    time.sleep(1)
    driver.close()


def alert_dismiss():
    driver = webdriver.Chrome()
    driver.get('http://demo.automationtesting.in/Alerts.html')
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(text(),'Alert with OK & Cancel')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'click the button to display a confirm box')]").click()
    time.sleep(1)
    alert = driver.switch_to.alert
    alert.dismiss()
    driver.refresh()
    time.sleep(1)
    driver.close()


def alert_textbox():
    driver = webdriver.Chrome()
    driver.get('http://demo.automationtesting.in/Alerts.html')
    time.sleep(1)
    driver.find_element(By.XPATH, "//a[contains(text(),'Alert with Textbox')]").click()
    driver.find_element(By.XPATH, "//button[contains(text(),'click the button to demonstrate the prompt box')]").click()
    time.sleep(1)
    alert1 = driver.switch_to.alert
    Alert(driver).send_keys('Frame Text')
    time.sleep(2)
    frame_text = alert1.text
    print(frame_text)
    alert1.accept()
    driver.refresh()
    time.sleep(1)
    driver.close()


alert_accept()
alert_dismiss()
alert_textbox()
