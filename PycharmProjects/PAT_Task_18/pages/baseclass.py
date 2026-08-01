from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return element

    def enter_text(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        element.send_keys(Keys.CONTROL, "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(text)
        return element

    def get_text(self, locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(locator))
            return element.text
        except:
            return None

    def wait_for_url_contains(self, text):
        self.wait.until(EC.url_contains(text))
        return text in self.driver.current_url

    def get_title(self):
        return self.driver.title

    def wait_for_presence(self, locator):
       return self.wait.until(EC.presence_of_element_located(locator))