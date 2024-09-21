from selenium.webdriver.common.by import By


class CreateAccount:

    create_account_link = (By.LINK_TEXT, "Create an Account")
    page_title = (By.CSS_SELECTOR, "h1.page-title span.base")
    first_name = (By.ID, "firstname")
    last_name = (By.ID, "lastname")
    email = (By.ID, "email_address")
    password = (By.ID, "password")
    confirm_password = (By.ID, "password-confirmation")
    submit_button = (By.CSS_SELECTOR, "button.action.submit.primary span")
    account_page_title = (By.CSS_SELECTOR, "h1.page-title span.base")

    def __init__(self, driver):

        self.driver = driver

    def goto_create_account(self):
        link_element = self.driver.find_element(*CreateAccount.create_account_link)
        link_element.click()

    def get_page_title(self):
        return self.driver.find_element(*CreateAccount.page_title).text

    def enter_firstname(self, firstname):
        firstname_element = self.driver.find_element(*CreateAccount.first_name)
        firstname_element.send_keys(firstname)

    def enter_lastname(self, lastname):
        lastname_element = self.driver.find_element(*CreateAccount.last_name)
        lastname_element.send_keys(lastname)

    def enter_email(self, email):
        email_element = self.driver.find_element(*CreateAccount.email)
        email_element.send_keys(email)

    def enter_password(self, password):
        password_element = self.driver.find_element(*CreateAccount.password)
        password_element.send_keys(password)

    def reenter_password(self, password):
        confirm_password_element = self.driver.find_element(*CreateAccount.confirm_password)
        confirm_password_element.send_keys(password)

    def submit(self):
        submit_element = self.driver.find_element(*CreateAccount.submit_button)
        submit_element.click()

    def get_error_message(self, locator):
        return self.driver.find_element(*locator)

    def refresh(self):
        self.driver.refresh()



