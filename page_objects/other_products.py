from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from random import choice


class OtherCategory:
    title = (By.ID, "page-title-heading")
    product_list = (By.CSS_SELECTOR, ".products.wrapper.grid ol li")
    product_name = (By.CLASS_NAME, "product-item-link")
    wishlist_icon = (By.CSS_SELECTOR, "a.action.towishlist")
    success_msg = (By.CSS_SELECTOR, "div[data-ui-id='message-success']")

    def __init__(self, driver):
        self.driver = driver
        self.product = None

    def select_product_other(self):
        product_list_element = self.driver.find_elements(*OtherCategory.product_list)
        self.product = choice(product_list_element)
        product_name = self.product.find_element(By.CLASS_NAME, "product-item-link").text
        action = ActionChains(self.driver)
        action.move_to_element(self.product).perform()
        return product_name

    def add_product_to_wishlist(self):
        self.product.find_element(*OtherCategory.wishlist_icon).click()





