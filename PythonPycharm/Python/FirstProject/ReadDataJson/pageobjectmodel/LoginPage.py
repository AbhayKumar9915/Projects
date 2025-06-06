from selenium.webdriver.common.by import By


class LoginPage:
    
    username_testbox_id = "username"
    password_txtbox_id = "password"
    login_button_xpath  = "//button[@type='submit']"
    
    def __init__(self, driver):
        self.driver = driver
        
    def enter_username(self, userName):
        self.driver.find_element(By.NAME, self.username_testbox_id).clear()
        self.driver.find_element(By.NAME, self.username_testbox_id).send_keys(userName)
            
    def enter_password(self, password):
        self.driver.find_element(By.NAME, self.password_txtbox_id).clear()
        self.driver.find_element(By.NAME, self.password_txtbox_id).send_keys(password)
        
    def click_login_button(self):
        self.driver.find_element(By.ID, self.login_button_xpath).click()