from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from random import choice
from page_objects.product_page import ProductPage


class ProductList:
    women_products = (By.CSS_SELECTOR, ".column.main > .products.wrapper > .products.list li")
    men_products_wrapper = (By.CSS_SELECTOR, "div.products.wrapper.grid")
    men_products = (By.CSS_SELECTOR, "ol li.item.product")
    product_name = (By.CSS_SELECTOR, "div.product.details a")
    colour = (By.CSS_SELECTOR, "div.swatch-attribute.color div div")
    add_button = (By.CSS_SELECTOR, "button[type='submit'] span")
    success_msg = (By.CSS_SELECTOR, "div[data-ui-id='message-success']")

    def __init__(self, driver):
        self.driver = driver
        self.product_men = None

    def select_product_women(self):
        # select a random product from the products pages
        products_element = self.driver.find_elements(*ProductList.women_products)
        select_product = choice(products_element)
        select_product.click()
        product_page = ProductPage(self.driver)
        return product_page

    def select_product_men(self):
        # select a random product from the products displayed based on the filter options selected
        product_wrapper_element = self.driver.find_element(*ProductList.men_products_wrapper)
        products_element = product_wrapper_element.find_elements(*ProductList.men_products)
        self.product_men = choice(products_element)

        # Hover on the product, else after the colour is selected control is redirected to the product detail page.
        action = ActionChains(self.driver)
        action.move_to_element(self.product_men).perform()

    def get_product_name(self):
        return self.product_men.find_element(*ProductList.product_name).text

    def select_colour(self):
        colour_elements = self.product_men.find_elements(*ProductList.colour)
        colour = choice(colour_elements)
        colour.click()

    def add_product(self):
        self.product_men.find_element(*ProductList.add_button).click()


