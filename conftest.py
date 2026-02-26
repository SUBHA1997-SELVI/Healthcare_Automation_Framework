import pytest
import os
from datetime import datetime
from utils.driver_factory import DriverFactory


def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browser in headless mode"
    )


@pytest.fixture(scope="function")
def setup(request):
    headless = request.config.getoption("--headless")
    driver = DriverFactory.get_driver(headless=headless)
    request.node.driver = driver
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = getattr(item, "driver", None)
        if driver:
            if not os.path.exists("reports/screenshots"):
                os.makedirs("reports/screenshots")

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"reports/screenshots/{item.name}_{timestamp}.png"
            driver.save_screenshot(screenshot_path)