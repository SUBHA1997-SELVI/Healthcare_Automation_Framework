import pytest
import os
from datetime import datetime
from utils.driver_factory import DriverFactory


@pytest.fixture(scope="function")
def setup():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()


# Hook to capture screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("setup")
        if driver:
            screenshots_dir = "reports/screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_name = f"{item.name}_{timestamp}.png"
            screenshot_path = os.path.join(screenshots_dir, screenshot_name)

            driver.save_screenshot(screenshot_path)
            print(f"\nScreenshot saved at: {screenshot_path}")