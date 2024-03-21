import pytest
from selenium import webdriver

driver = None

@pytest.hookimpl(hookwrapper=True,tryfirst=True)
def pytest_runtest_makereport(item,call):
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        img = driver.get_screenshot_as_png()

@pytest.fixture(scope="session",autouse=True)
def init():
    global driver
    driver = webdriver.Chrome()