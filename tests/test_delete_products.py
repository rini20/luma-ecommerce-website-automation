from page_objects.logout import Logout
from page_objects.shopping_cart import ShoppingCart
from utilities.base_class import BaseClass
from page_objects.login import Login
from test_data import test_users_credentials as UC
from selenium.common import TimeoutException
import pytest


class TestDelete(BaseClass):
    @pytest.fixture
    def setup(self):
        login = Login(self.driver)
        login.click_sign_in()
        login.enter_email(UC.existing_username)
        login.enter_password(UC.existing_password)
        login.sign_in()
        yield
        logout = Logout(self.driver)
        logout.click_actions()
        logout.click_logout()

    def test_delete(self, setup):
        cart = ShoppingCart(self.driver)
        try:
            self.wait_for_visibility_of_element(cart.cart_quantity)
        except TimeoutException:
            print("The cart is empty")
            assert cart.cart_quantity == '0'

        else:
            # get initial product count from cart
            initial_count = cart.get_item_count()

            # edit the cart and get product price and cart subtotal
            cart.view_edit_cart()
            cart.get_item()
            product_price = cart.get_item_price()
            initial_subtotal = cart.get_subtotal()

            # delete a product and get for the update count
            cart.delete_item()
            self.wait_for_visibility_of_element(cart.cart_quantity)
            final_count = cart.get_item_count()

            # calculate the final cart value
            final_subtotal = cart.get_subtotal()
            expected_cart_value = initial_subtotal - product_price

            # validate the item count and total price
            assert final_count == initial_count - 1
            assert final_subtotal == expected_cart_value
