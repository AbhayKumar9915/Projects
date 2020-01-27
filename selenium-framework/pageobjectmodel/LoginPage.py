class LoginPage():
    
    username_testbox_id = "txtUsername"
    password_txtbox_id = "txtPassword"
    login_button_id  = "btnLogin"
    
    def __init__(self, driver):
        self.driver = driver
        
        
    def enter_username(self,userName):
        self.driver.find_element_by_id(self.username_testbox_id).clear()
        self.driver.find_element_by_id(self.username_testbox_id).send_keys(userName)
            
    def enter_password(self,password):
        self.driver.find_element_by_id(self.password_txtbox_id).clear()
        self.driver.find_element_by_id(self.password_txtbox_id).send_keys(password)
        
    def click_login_button(self):
        self.driver.find_element_by_id(self.login_button_id).click() 