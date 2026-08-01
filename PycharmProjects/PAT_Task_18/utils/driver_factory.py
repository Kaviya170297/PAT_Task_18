import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():
    """
    Returns a configured Chrome WebDriver.
    Reads env vars so the same code works locally and in CI:
      HEADLESS=true/false
    """
    options = Options()

    headless = os.getenv("HEADLESS", "false").lower() == "true"
    if headless:
        options.add_argument("--headless=new")

    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    # No `service=` argument -> Selenium Manager resolves the driver itself.
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)  # kept small; we rely mainly on explicit waits in BasePage
    return driver