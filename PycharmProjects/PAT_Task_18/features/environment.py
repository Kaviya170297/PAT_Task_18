import os
from utils.driver_factory import get_driver

SCREENSHOT_DIR = os.path.join(os.path.dirname(__file__), "", "reports", "screenshots")


def before_all(context):
    """Runs once before the entire test run."""
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)
    context.config.setup_logging()


def before_feature(context, feature):
    """Runs before each .feature file."""
    print(f"Running feature: {feature.name}")
    pass  # hook point for per-feature setup if ever needed


def before_scenario(context, scenario):
    """
    Runs before EVERY scenario.
    Creates a fresh browser session so scenarios never leak state
    into one another (a core testing-independence principle).
    """
    print(f"Starting scenario: {scenario.name}")
    context.driver = get_driver()


def after_scenario(context, scenario):
    """
    Runs after every scenario.

    - Takes a screenshot when the scenario fails.
    - Closes the browser safely.
    """

    # Take screenshot only if driver exists and is still active
    if (
        scenario.status == "failed"
        and hasattr(context, "driver")
        and context.driver is not None
    ):
        safe_name = (
            scenario.name
            .replace(" ", "_")
            .replace("/", "_")
        )

        screenshot_path = os.path.join(
            SCREENSHOT_DIR,
            f"{safe_name}.png"
        )

        try:
            context.driver.save_screenshot(
                screenshot_path
            )

            print(
                f"Screenshot saved: {screenshot_path}"
            )

        except Exception as error:
            print(
                f"Could not capture screenshot: {error}"
            )

    # Quit only when driver is not already closed
    if (
        hasattr(context, "driver")
        and context.driver is not None
    ):
        try:
            context.driver.quit()

        except Exception as error:
            print(
                f"Could not close browser: {error}"
            )

        finally:
            context.driver = None

def after_all(context):
    """Runs once after the entire test run."""
    print("All scenarios finished.")
    pass