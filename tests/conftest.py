from selenium import webdriver
import pytest


URL = "https://magento.softwaretestingboard.com/"

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope='class')
def setup_teardown_invoke_browser(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        option = webdriver.ChromeOptions()
        option.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=option)
        driver.get(URL)
        driver.implicitly_wait(10)
    elif browser_name == 'firefox':
        option = webdriver.FirefoxOptions()
        # option.add_argument("--start-maximized")
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(URL)
        driver.implicitly_wait(10)

    request.cls.driver = driver
    yield
    driver.quit()



