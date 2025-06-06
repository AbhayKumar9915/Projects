import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

try:
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://demo.automationtesting.in/Static.html')
    driver.execute_script("window.scrollTo(0, 200)")
    source_loc = driver.find_element(By.ID, 'angular')
    drop_loc = driver.find_element(By.ID, 'droparea')
    action = ActionChains(driver)
    action.drag_and_drop(source_loc,drop_loc).perform()
    time.sleep(2)
    source_loc = driver.find_element(By.ID, 'node')
    drop_loc = driver.find_element(By.ID, 'droparea')
    action = ActionChains(driver)
    action.drag_and_drop(source_loc,drop_loc).perform()
    time.sleep(2)
    assert driver.title == 'Drag and Drop'
    print('Test')
    driver.close()
except Exception as e:
    print(e)