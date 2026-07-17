import pytest
from utils.driver import get_driver
from utils.screenshot import take_screenshot


@pytest.fixture
def setup():

    driver = get_driver()

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs["setup"]

        take_screenshot(driver, item.name)