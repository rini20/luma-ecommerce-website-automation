from selenium.webdriver.common.by import By


class Login:

    sign_in_link = (By.LINK_TEXT, "Sign In")
    email = (By.CSS_SELECTOR, "input#email")
    password = (By.CSS_SELECTOR, "input#pass")
    sing_in_button = (By.ID, "send2")
    welcome_msg = (By.CSS_SELECTOR, "li.greet.welcome span.logged-in")

    def __init__(self, driver):
        self.driver = driver

    def click_sign_in(self):
        return self.driver.find_element(*Login.sign_in_link).click()

    def enter_email(self, email):
        email_element = self.driver.find_element(*Login.email)
        email_element.send_keys(email)

    def enter_password(self, password):
        password_element = self.driver.find_element(*Login.password)
        password_element.send_keys(password)

    def sign_in(self):
        self.driver.find_element(*Login.sing_in_button).click()








