import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

# Mouse Hover Program
try:
    driver=webdriver.Chrome()
    driver.get('https://demo.automationtesting.in/AutoComplete.html')
    driver.maximize_window()
    element_xpath = "//span[@class='fa fa-facebook-square']"
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, element_xpath)))
    driver.find_element(By.ID,'searchbox').send_keys('a')
    time.sleep(2)
    hover = driver.find_element(By.XPATH, "//a[contains(text(),'Angola')]")
    first_h = ActionChains(driver).move_to_element(hover)
    first_h.perform()
    time.sleep(2)
    first_h.click()
    time.sleep(2)
    driver.close()
except Exception as e:
    print(e)

# Alert handling
try:
    driver=webdriver.Chrome()
    driver.get('https://demo.automationtesting.in/Alerts.html')
    driver.maximize_window()
    print(driver.title)
    print(driver.current_url)
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'alert box:')]").click()
    time.sleep(2)
    Alert(driver).accept()
    #alert = driver.switch_to.alert
    #alert.accept()
    time.sleep(2)
except Exception as e:
    print(e)

# Window handling
try:
    driver=webdriver.Chrome()
    driver.get('https://demo.automationtesting.in/Windows.html')
    #driver.maximize_window()
    print(driver.title)
    print(driver.current_url)
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[contains(text(),'click')]").click()
    time.sleep(2)
    wh1 = driver.window_handles[1]
    driver.switch_to.window(wh1)
    driver.find_element(By.ID, "navbarDropdown").click()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(2)
except Exception as e:
    print(e)

# iFrame handling
try:
    driver=webdriver.Chrome()
    driver.get('https://demo.automationtesting.in/Frames.html')
    #driver.maximize_window()
    print(driver.title)
    print(driver.current_url)
    time.sleep(2)
    iframe_id = 'singleframe'
    driver.switch_to.frame(driver.find_element(By.ID, iframe_id))
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys('Test')
    time.sleep(2)
except Exception as e:
    print(e)