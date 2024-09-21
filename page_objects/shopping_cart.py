from selenium.webdriver.common.by import By
from random import choice


class ShoppingCart:

    view_edit = (By.CSS_SELECTOR, "a.action.viewcart span")
    item_table = (By.ID, "shopping-cart-table")
    cart_item = (By.CSS_SELECTOR, "tbody.cart.item")
    item_price = (By.CSS_SELECTOR, "tr.item-info td.subtotal .price")
    delete_icon = (By.CSS_SELECTOR, "a.action-delete[title='Remove item']")
    cart_quantity = (By.CSS_SELECTOR, "span.counter.qty .counter-number")
    subtotal = (By.CSS_SELECTOR, "td.amount span.price")

    def __init__(self, driver):
        self.driver = driver
        self.item = None

    def get_item_count(self):
        quantity_element = self.driver.find_element(*ShoppingCart.cart_quantity)
        item_count = int(quantity_element.text)
        quantity_element.click()
        return item_count

    def view_edit_cart(self):
        self.driver.find_element(*ShoppingCart.view_edit).click()

    def get_item(self):
        item_table_element = self.driver.find_element(*ShoppingCart.item_table)
        cart_items = item_table_element.find_elements(*ShoppingCart.cart_item)
        self.item = choice(cart_items)

    def get_item_price(self):
        item_price_element = self.item.find_element(*ShoppingCart.item_price).text
        price = item_price_element.replace("$", '')
        return float(price)

    def delete_item(self):
        self.item.find_element(*ShoppingCart.delete_icon).click()

    def get_subtotal(self):
        subtotal_element = self.driver.find_element(*ShoppingCart.subtotal).text
        price = subtotal_element.replace('$', '')
        return float(price)

