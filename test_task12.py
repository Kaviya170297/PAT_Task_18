import time
import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

#webdriver setup:
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


from selenium.webdriver.common.by import By
BASE_URL = "https://www.guvi.in/"
LOGIN_URL = "https://www.guvi.in/sign-in/"

@pytest.mark.guvi
def test_liveclasses(setup):
    driver = setup
    driver.get(BASE_URL)
    driver.find_element(By.XPATH,("//div[@id='solutions']//p[(text()='LIVE Classes')]/parent::div")).click()
    time.sleep(2)
    driver.quit()

#Live class parent, child, second sibling , href parent, Ancestor, all following sibling, preceding elements xpath:
# Live classes:
# Parent:
# //div[@id='solutions']//p[(text()='LIVE Classes')]/parent::div
# Child:
# //div[@id='solutions']//p[(text()='LIVE Classes')][1]
# Second sibling: there is only one sibling
# (//div[@id='solutions']//p[(text()='LIVE Classes')]following-sibling::div)[2]
# Href parent:
# //a[@href="#liveClass"]
# Ancestor:
# //div[@id='solutions']//p[(text()='LIVE Classes')]/ancestor::*
# Locate all following sibling:
# No second sibling for this
# (//div[@id='solutions']//p[(text()='LIVE Classes')]/following-sibling::*)[1]
# Preceding:
# //div[@id='solutions']//p[(text()='LIVE Classes')]/preceding::*

#Below are Courses parent, child, second sibling , href parent, Ancestor, all following sibling, preceding elements xpath:
# Parent:
# //div[@id='solutions']//p[(text()='Courses')]/parent::div
# Child:
# //div[@id='solutions']//p[(text()='Courses')][1]
# Second sibling: no second sibling so giving 1:
# (//div[@id='solutions']//p[(text()='Courses')]/following-sibling::*)[1]
# Href parent:
# //a[@href="#Courses"]
# Ancestor:
# //div[@id='solutions']//p[(text()='Courses')]/ancestor::*
# Locate all following sibling:
# //div[@id='solutions']//p[(text()='Courses')]/following-sibling::*
# Preceding:
# //div[@id='solutions']//p[(text()='Courses')]/preceding::*

#Below are Practice parent, child, second sibling , href parent, Ancestor, all following sibling, preceding elements xpath:
# PArent:
# //div[@id='solutions']//p[(text()='Practice')]/parent::div
# Child:
# //div[@id='solutions']//p[(text()='Practice')][1]
# Second sibling: No second sibling:
# //div[@id='solutions']//p[(text()='Practice')]/following-sibling::*
# //div[@id='solutions']//p[(text()='Practice')]/following-sibling::*[1]
# Href parent:
# //a[@href="#Practice"]
# Ancestor:
# //div[@id='solutions']//p[(text()='Practice')]/ancestor::*
# Locate all following sibling:
# //div[@id='solutions']//p[(text()='Practice')]/following-sibling::*
# Preceding:
# //div[@id='solutions']//p[(text()='Practice')]/preceding::*

#Below are Resources parent, child, second sibling , href parent, Ancestor, all following sibling, preceding elements xpath:
# Parent:
# //div[@id='solutions']//p[(text()='Resources')]/parent::div
# Child:
# //div[@id='solutions']//p[(text()='Resources')][1]
# Second Sibling: there is only one sibling
# //div[@id='solutions']//p[(text()='Resources')]/following-sibling::*
# //div[@id='solutions']//p[(text()='Resources')]/following-sibling::*[1]
# Href parent:
# //a[@href="#Resources"]
# Ancestor:
# //div[@id='solutions']//p[(text()='Resources')]/ancestor::*
# Locate all following sibling:
# //div[@id='solutions']//p[(text()='Resources')]/following-sibling::*
# Preceding:
# //div[@id='solutions']//p[(text()='Resources')]/preceding::*

#Below are Our products parent, child, second sibling , href parent, Ancestor, all following sibling, preceding elements xpath:
# Parent:
# //div[@id='solutions']//p[(text()='Our Products')]/parent::div
# Child:
# //div[@id='solutions']//p[(text()='Our Products')][1]
# Second sibling: there is only one sibling
# //div[@id='solutions']//p[(text()='Our Products')]/following-sibling::*
# (//div[@id='solutions']//p[(text()='Our Products')]/following-sibling::*)[2]
# Href parent:
# //*[@href]/parent::*]
# Ancestor:
# //div[@id='solutions']//p[(text()='Our Products')]/ancestor::*
# Locate all following sibling:
# //div[@id='solutions']//p[(text()='Our Products')]/following-sibling::*
# Preceding:
# //div[@id='solutions']//p[(text()='Our Products')]/preceding::*

#Below are Login button  parent, child, second sibling , href parent, Ancestor, all following sibling, preceding elements xpath:
# Parent:
# //button[@id='login-btn']/parent::div
# Child:
# //button[@id='login-btn'][1]
# //button[@id='login-btn']/parent::div/child::*[1]
# Second sibling: there is only one sibling
# //button[@id='login-btn']/following-sibling::*
# (//button[@id='login-btn']/following-sibling::button)[2]
# Href parent:
# //*[@href]/parent::*]
# Ancestor:
# //button[@id='login-btn']/ancestor::*
# Locate all following sibling:
# //button[@id='login-btn']/following-sibling::*
# Preceding:
# //button[@id='login-btn']/preceding::*

#Below are Signup button  parent, child, second sibling , href parent, Ancestor, all following sibling, preceding elements xpath:
# Parent:
# //button[text()='Sign up']/parent::div
# Child:
# //button[text()='Sign up']/parent::div/child::*[1]
# Second sibling: there is no sibling
# //button[text()='Sign up']/following-sibling::*
# Href parent:
# //*[@href]/parent::*]
# Ancestor:
# //button[text()='Sign up']/ancestor::*
# Locate all following sibling:
# //button[text()='Sign up']/following-sibling::*
# Preceding:
# //button[text()='Sign up']/preceding::*