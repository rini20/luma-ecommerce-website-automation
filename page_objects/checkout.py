from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.support.ui import Select
from random import choice


class CheckOut:

    cart = (By.CSS_SELECTOR, "a.action.showcart")
    quantity = (By.CSS_SELECTOR, "span.counter-label")
    proceed_button = (By.ID, "top-cart-btn-checkout")
    address = (By.CSS_SELECTOR, ".step-title")
    shipping_method = (By.CSS_SELECTOR, "tr.row td.col-method input")
    street_address_1 = (By.CSS_SELECTOR, "input.input-text[name='street[0]']")
    street_address_2 = (By.CSS_SELECTOR, "input.input-text[name='street[1]']")
    city = (By.CSS_SELECTOR, "input.input-text[name='city']")
    state = (By.NAME, "region_id")
    zipcode = (By.CSS_SELECTOR, "input.input-text[name='postcode']")
    country = (By.CSS_SELECTOR, "select.select[name='country_id']")
    phone = (By.CSS_SELECTOR, "input.input-text[name='telephone']")
    next = (By.CSS_SELECTOR, "button.button.action span")
    payment_page = (By.CSS_SELECTOR,".payment-group div.step-title")
    checkout_button = (By.CSS_SELECTOR, "button.action.primary.checkout span")
    order_number = (By.CSS_SELECTOR, ".checkout-success p a.order-number")
    success = (By.CSS_SELECTOR, "div.checkout-success p")

    def __init__(self, driver):
        self.driver = driver

    def get_shopping_cart(self):
        self.driver.find_element(*CheckOut.cart).click()

    def proceed_to_checkout(self):
        self.driver.find_element(*CheckOut.proceed_button).click()

    def enter_street_1(self, street_1):
        street_1_element = self.driver.find_element(*CheckOut.street_address_1)
        street_1_element.send_keys(street_1)

    def enter_street_2(self, street_2):
        street_1_element = self.driver.find_element(*CheckOut.street_address_2)
        street_1_element.send_keys(street_2)

    def enter_city(self, city):
        city_element = self.driver.find_element(*CheckOut.city)
        city_element.send_keys(city)

    def select_state(self):
        state_element = self.driver.find_element(*CheckOut.state)
        select = Select(state_element)
        select.select_by_index(4)

    def enter_zipcode(self, zipcode):
        zipcode_element = self.driver.find_element(*CheckOut.zipcode)
        zipcode_element.send_keys(zipcode)

    def select_country(self):
        country_element = self.driver.find_element(*CheckOut.country)
        select = Select(country_element)
        select.select_by_value("IN")

    def enter_phone(self, phone):
        phone_element = self.driver.find_element(*CheckOut.phone)
        phone_element.send_keys(phone)

    def select_shipping_method(self):
        method_element = self.driver.find_elements(*CheckOut.shipping_method)
        choice(method_element).click()
        next_element = self.driver.find_element(*CheckOut.next)
        next_element.click()

    def click_checkout(self):
        checkout_button_element = self.driver.find_element(*CheckOut.checkout_button)
        for _ in range(2):
            try:
                checkout_button_element.click()
                break
            except ElementClickInterceptedException:
                continue

    def get_success_msg(self):
        return self.driver.find_element(*CheckOut.success).text
