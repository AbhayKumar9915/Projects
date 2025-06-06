from selenium.webdriver.common.by import By


class HomePage:
    
    welcome_link_xpath = "//*[@class='oxd-userdropdown-tab']"
    logout_link_xpath = "//a[contains(text(),'Logout')]"
    
    def __init__(self, driver):
        self.driver = driver
       
    def click_wlcome(self):
        self.driver.find_element(By.XPATH, self.welcome_link_xpath).click()
        
    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_link_xpath).click()