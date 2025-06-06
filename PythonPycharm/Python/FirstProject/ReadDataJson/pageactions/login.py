from selenium import webdriver
import time
import unittest
from FirstProject.ReadDataJson.pageobjectmodel.LoginPage import LoginPage
from FirstProject.ReadDataJson.pageobjectmodel.HomePage import HomePage

import json

with open('C:\\Users\\ab1kumar\\Pycharm Projects\\Python\\FirstProject\\ReadDataJson\\datascheame\\Data.json', 'r') as data_files:
    data = json.loads(data_files.read())


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get(data['URL'])
        login = LoginPage(driver)
        login.enter_username(data['username'])
        login.enter_password(data['password'])
        login.click_login_button()
        
    def test_logout(self):  
        driver = self.driver  
        homepage = HomePage(driver)
        homepage.click_wlcome()
        time.sleep(1)
        homepage.click_logout()
        time.sleep(2)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print('Test Successful')


if __name__ == '__main__':
    unittest.main()
