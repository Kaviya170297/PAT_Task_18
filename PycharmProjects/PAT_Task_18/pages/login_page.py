from selenium.webdriver.common.by import By
from pages.baseclass import BasePage

class LoginPage(BasePage):
    # Locators
    email_input = (By.XPATH, "//input[@placeholder='Enter your mail']")
    password_input = (By.XPATH, "//input[@id=':r2:']")
    login_button = (By.XPATH, "//button[@class='primary-btn sign-in-pad']")
    error_message = (By.XPATH, "//p[contains(@class,'Mui-error')]")


    def enter_username(self, username):
        self.enter_text(self.email_input, username)

    def enter_password(self, password):
       self.enter_text(self.password_input, password)

    def click_login(self):
        self.click_element(self.login_button)

    def get_error_message(self):
        return self.get_text(self.error_message)

    # Validations
    def validate_input_boxes(self):
        username_box = self.wait_for_presence(self.email_input)
        password_box = self.wait_for_presence(self.password_input)
        assert username_box.is_displayed(), "Username input box not visible"
        assert password_box.is_displayed(), "Password input box not visible"
        print("username and password input boxes are visible and interactable.")

    def validate_submit_button(self):
        login_btn = self.wait_for_presence(self.login_button)
        assert login_btn.is_displayed(), "Login button not visible"
        assert login_btn.is_enabled(), "Login button disabled"