import time
import XLSUtils
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
path = "C:\\Users\\ab1kumar\\Pycharm Projects\\Python\\FirstProject\\ReadData\\Test.xlsx"
rows = XLSUtils.getRowCount(path,"Sheet1")

try:
    for r in range(2, rows+1):
        username = XLSUtils.readData(path, "Sheet1", r, 1)
        print(username)
        password = XLSUtils.readData(path, "Sheet1", r, 2)
        print(password)
        username_locator="//*[@name='username']"
        WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH,username_locator)))
        driver.find_element(By.XPATH,username_locator).send_keys(username)
        driver.find_element(By.NAME,"password").send_keys(password)
        driver.find_element(By.XPATH,"//button[@type='submit']").click()

        if driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":
            print('Test Case Pass')
            element_xpath = "//*[@class='oxd-userdropdown-tab']"
            WebDriverWait(driver,10).until(ec.presence_of_element_located((By.XPATH, element_xpath)))
            XLSUtils.writeData(path, "Sheet1", r, 3,"Test Passed")
            driver.find_element(By.XPATH,element_xpath).click()
            time.sleep(2)
            driver.find_element(By.XPATH,"//a[contains(text(),'Logout')]").click()
        else:
            print('Test case failed')
            XLSUtils.writeData(path, "Sheet1", r, 3, "Test Failed")
    driver.close()
except Exception as e:
    print(e)
