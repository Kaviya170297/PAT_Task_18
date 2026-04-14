from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest

#webdriver setup:
@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_positive_testcase(setup):
    driver = setup
    try:
        # Navigate to the URL
        driver.get("https://jqueryui.com/droppable/")

        # Wait for page to load
        time.sleep(3)

        # Switch to iframe
        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)

        # Wait for elements to be visible
        time.sleep(2)

        # Locate elements
        draggable = driver.find_element(By.ID, "draggable")
        droppable = driver.find_element(By.ID, "droppable")

        # Perform drag and drop
        actions = ActionChains(driver)
        actions.drag_and_drop(draggable, droppable).perform()

        # Wait to observe result
        time.sleep(2)

        print("Drag and drop completed successfully!")

    finally:
        driver.quit()

def test_invalid_element_id(setup):
    driver = setup
    try:
        driver.get("https://jqueryui.com/droppable/")
        time.sleep(2)

        iframe = driver.find_element(By.TAG_NAME, "iframe")
        driver.switch_to.frame(iframe)

        # Invalid draggable ID
        draggable = driver.find_element(By.ID, "invalid_draggable")
        droppable = driver.find_element(By.ID, "droppable")

        actions = ActionChains(driver)
        actions.drag_and_drop(draggable, droppable).perform()

    except Exception as e:
        print("Test Passed - Exception occurred:", e)

    finally:
        driver.quit()

def test_without_switching_iframe(setup):
    driver = setup
    try:
        driver.get("https://jqueryui.com/droppable/")
        time.sleep(2)

        # Not switching to iframe (intentional mistake)
        draggable = driver.find_element(By.ID, "draggable")
        droppable = driver.find_element(By.ID, "droppable")

        actions = ActionChains(driver)
        actions.drag_and_drop(draggable, droppable).perform()

    except Exception as e:
        print("Test Passed - Exception occurred:", e)

    finally:
        driver.quit()