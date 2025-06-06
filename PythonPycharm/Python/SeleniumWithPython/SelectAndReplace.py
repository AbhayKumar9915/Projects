import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

select_xpath = "//select[@id='dropdown-class-example']"
replace_xpath = "//select[@id='dropdown-class-example']/option[contains(text(),'?')]"

dropdown = Select(driver.find_element(By.XPATH, select_xpath))
dropdown.select_by_visible_text('Option3')
time.sleep(1)
dropdown.select_by_index(1)
time.sleep(1)
dropdown.select_by_value('option2')
time.sleep(1)
print("Select Fn Passed")


def replace_fun(data):
    driver.find_element(By.XPATH,replace_xpath.replace('?', data)).click()


replace_fun('Option1')
print("Replace Fn Passed")
time.sleep(2)

# For getting number of options in dropdown and all values
all_options = dropdown.options
print(len(all_options))
for opt in all_options:
    print(opt.text)

driver.quit()
