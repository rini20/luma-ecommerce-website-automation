from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.mark.usefixtures('setup_teardown_invoke_browser')
class BaseClass:

    def wait_for_visibility_of_element(self, locator):
        wait = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return wait

    def wait_for_visibility_of_all_elements(self, locator):
        wait = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return wait

    def wait_for_text_presence(self, locator, text):
        wait = WebDriverWait(self.driver,10).until(EC.text_to_be_present_in_element(locator, text))
        return wait

    def wait_for_element_to_be_clickable(self, locator):
        wait = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        return wait

