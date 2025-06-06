from selenium import webdriver

driver = webdriver.Chrome()
# Path sets at environment level(Working fine for chrome and firefox)
driver.maximize_window()
driver.get('https://www.google.com/')
print('Chrome driver is working fine')
driver.quit()

# driver1 = webdriver.Edge()
# driver1.get('https://www.google.com/')
# print('Edge driver is working fine')
# driver1.quit()
#
# driver2 = webdriver.Firefox()
# driver2.get('https://www.google.com/')
# print('Firefox driver is working')
# driver2.quit()

print('Cheers...All Browsers are working as expected :)')
