from selenium.webdriver.common.by import By
from pages.baseclass import BasePage

class DashboardPage(BasePage):
    # Locators
    popup_close = (By.XPATH, "//img[@src='/images/commonComponents/commonPopup/commonPopupCloseIcon.svg']")
    profile_icon = (By.XPATH, "//img[@id='profile-click-icon']")
    logout_button = (By.XPATH, "//div[normalize-space()='Log out']")


    # Actions
    def close_popup(self):
        self.click_element(self.popup_close)

    def logout(self):
        self.click_element(self.profile_icon)
        self.click_element(self.logout_button)


    #Assertion

    def verify_logout(self):
        return "GUVI" in self.get_title()

    def verify_dashboard_loaded(self):
        return self.wait_for_url_contains("dashboard")