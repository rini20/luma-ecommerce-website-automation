from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from random import choice
from time import sleep

class ProductPage:

    in_stock = (By.CSS_SELECTOR, "[title='Availability']")
    product_title = (By.CSS_SELECTOR,".page-title span")
    images = (By.CSS_SELECTOR, ".fotorama__stage__shaft.fotorama__grab")
    image_count = (By.CSS_SELECTOR,"div.fotorama__stage__frame")
    image_arrow = (By.CSS_SELECTOR, ".fotorama__arr.fotorama__arr--next")
    close_image = (By.CSS_SELECTOR,".fotorama__fullscreen-icon")
    size = (By.CSS_SELECTOR, ".swatch-attribute-options.clearfix div.swatch-option.text")
    colour = (By.CSS_SELECTOR, ".swatch-attribute-options.clearfix div.swatch-option.color")
    quantity = (By.CSS_SELECTOR, "input[id='qty']")
    add_button = (By.CSS_SELECTOR,"#product-addtocart-button")
    confirmation_msg_add = (By.CSS_SELECTOR, "div.message-success div")
    wishlist_icon = (By.LINK_TEXT, "Add to Wish List")
    confirmation_msg_wishlist = (By.CSS_SELECTOR, "div[data-ui-id='message-success']")

    def __init__(self, driver):
        self.driver = driver

    def get_product_name(self):
        return self.driver.find_element(*ProductPage.product_title).text

    def browse_product_images(self):
        images_element = self.driver.find_element(*ProductPage.images)
        images_count_element = images_element.find_elements(*ProductPage.image_count)
        images_element.click()
        for _ in range(len(images_count_element)-1):
            try:
                self.driver.find_element(*ProductPage.image_arrow).click()
                sleep(1)
            except ElementClickInterceptedException:
                break
        self.driver.find_element(*ProductPage.close_image).click()

    def select_size(self):
        size_element = self.driver.find_elements(*ProductPage.size)
        select_size = choice(size_element)
        select_size.click()

    def select_colour(self):
        colour_element = self.driver.find_elements(*ProductPage.colour)
        select_colour = choice(colour_element)
        select_colour.click()

    def enter_quantity(self, count):
        quantity_element = self.driver.find_element(*ProductPage.quantity)
        quantity_element.send_keys(Keys.CONTROL + "a")
        quantity_element.send_keys(Keys.DELETE)
        quantity_element.send_keys(count)

    def add_product(self):
        self.driver.find_element(*ProductPage.add_button).click()

    def add_to_wishlist(self):
        self.driver.find_element(*ProductPage.wishlist_icon).click()

    def get_add_msg(self):
        return self.driver.find_element(*ProductPage.confirmation_msg_wishlist).text





