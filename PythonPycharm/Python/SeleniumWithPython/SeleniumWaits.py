import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
driver.implicitly_wait(10)
# implicitly wait for every action(elements) for 10 seconds
assert 'OrangeHRM' in driver.title
driver.find_element(By.NAME, 'txtUsername').send_keys('Admin')
driver.find_element(By.NAME, 'txtPassword').send_keys('admin123')
driver.find_element(By.CLASS_NAME,'button').click()
driver.quit()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.makemytrip.com/flights/')
driver.find_element(By.XPATH, "//a[contains(text(),'Search')]").click()
element_xpath = "(//*[@class='box'])[1]"
# Explicit waits for maximum 10 seconds, if found before 10 sec and condition fulfilled its goes to next step
wait_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
wait_element.click()
driver.find_element(By.XPATH,"(//*[@class='box'])[15]").click()
time.sleep(3)
driver.quit()
