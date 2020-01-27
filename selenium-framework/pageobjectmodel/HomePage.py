class HomePage():
    
    welcome_link_id = "welcome"
    logout_link_xpath = "//*[@href='/index.php/auth/logout']"
    
    def __init__(self, driver):
        self.driver = driver
       
    def click_wlcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()
        
    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()        