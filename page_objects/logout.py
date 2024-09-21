from selenium.webdriver.common.by import By


class Logout:

    actions = (By.CSS_SELECTOR, "button.action.switch")
    logout = (By.CSS_SELECTOR, ".customer-menu ul li.authorization-link a")

    def __init__(self, driver):
        self.driver = driver

    def click_actions(self):
        return self.driver.find_element(*Logout.actions).click()

    def click_logout(self):
        return self.driver.find_element(*Logout.logout).click()
