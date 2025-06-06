import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# for getting numbers of input boxes by there attributes
driver = webdriver.Chrome()
driver.get('http://demo.automationtesting.in/Register.html')
input_boxes = driver.find_elements(By.TAG_NAME,'input')
print(len(input_boxes))
for inputs in input_boxes:
    attribute_type = inputs.get_attribute('value') or inputs.get_attribute('ng-model') or inputs.get_attribute('type')
    print(attribute_type)
driver.quit()

# Valid and broken links on web url by checking there url status code by using requests module
driver = webdriver.Chrome()
driver.get('https://www.google.com/')
links = driver.find_elements(By.TAG_NAME, 'a')
for link in links:
    href = link.get_attribute('href')
    if requests.head(link.get_attribute('href'), verify=False).status_code == 200:
        print('Valid Url', href)
    else:
        print('Broken Url', href)
driver.quit()

# for getting all the links on web page
driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')
links = driver.find_elements(By.TAG_NAME, 'a')
for link in links:
    href = link.get_attribute('href')
    if href is not None:  # To remove None and javascript texts
        if href != "javascript:;":
            print(href)
driver.quit()
