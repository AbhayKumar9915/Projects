from selenium import webdriver
import pytest


def test_Google():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://www.google.com')
    assert driver.title == "Google"
    driver.quit()


def test_Facebook():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://www.facebook.com')
    assert driver.title == "Facebook – log in or sign up"
    driver.quit()


def test_Instagram():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://www.instagram.com')
    assert driver.title == "Instagram"
    driver.quit()


def test_Gmail():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://www.gmail.com')
    assert driver.title == "Gmail"
    driver.quit()

