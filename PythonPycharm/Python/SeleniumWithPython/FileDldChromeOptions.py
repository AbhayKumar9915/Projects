from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chromeOptions = Options()
# Download file in desired directory
pref = {'download.default_directory': r'C:\Users\ab1kumar\Pycharm Projects\Python\SeleniumWithPython'}
chromeOptions.add_experimental_option('prefs', pref)

driver = webdriver.Chrome(options=chromeOptions)
driver.get("http://demo.automationtesting.in/FileDownload.html")

# Download text file
driver.find_element(By.ID,'textbox').send_keys('Text File Download')
driver.find_element(By.XPATH,"//button[@id='createTxt']").click()
driver.find_element(By.ID, 'link-to-download').click()
time.sleep(2)

# Download pdf file
driver.find_element(By.ID,'pdfbox').send_keys('Pdf File Download')
driver.find_element(By.XPATH,"//button[@id='createPdf']").click()
driver.find_element(By.ID, 'pdf-link-to-download').click()
time.sleep(5)

# Open downloaded file in Chrome downloads
try:
    driver.get("chrome://downloads/")
    driver.find_element(By.TAG_NAME,'downloads-manager').send_keys(Keys.TAB)
    driver.find_element(By.TAG_NAME,'downloads-manager').send_keys(Keys.TAB)
    # Opening Text file
    driver.find_element(By.TAG_NAME,'downloads-manager').send_keys(Keys.DOWN)
    driver.find_element(By.TAG_NAME,'downloads-manager').send_keys(Keys.ENTER)
    # Opening pdf file
    driver.find_element(By.TAG_NAME,'downloads-manager').send_keys(Keys.UP)
    driver.find_element(By.TAG_NAME,'downloads-manager').send_keys(Keys.ENTER)
    time.sleep(3)
except Exception as e:
    print(e)

driver.quit()
