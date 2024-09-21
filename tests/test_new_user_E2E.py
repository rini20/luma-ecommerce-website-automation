from page_objects.logout import Logout
from utilities.base_class import BaseClass
from page_objects.login import Login
from page_objects.menu import Menu
from page_objects.checkout import CheckOut
from test_data import test_users_credentials as UC
from test_data.E2E_test_data import E2ETestData
import pytest


class TestEndToEnd(BaseClass):

    # test sign-in
    def test_login(self):
        login = Login(self.driver)
        login.click_sign_in()
        login.enter_email(UC.new_username)
        login.enter_password(UC.new_password)
        login.sign_in()
        element = self.wait_for_text_presence(login.welcome_msg, 'Welcome')
        assert element

    # select random item from women's category and add to cart
    def test_add_product_women(self):
        menu = Menu(self.driver)
        menu.select_category('Women')
        product_list = menu.select_submenu_women()

        # select an item and add to cart, if item is out of stock add to wishlist
        product_page = product_list.select_product_women()
        text = "IN STOCK"
        in_stock = self.wait_for_text_presence(product_page.in_stock, text)
        product_name = product_page.get_product_name()
        if in_stock:
            product_page.select_size()
            product_page.select_colour()
            product_page.enter_quantity(2)
            product_page.add_product()
            confirmation_msg = self.wait_for_visibility_of_element(product_page.confirmation_msg_add).text
            assert f"You added {product_name}" in confirmation_msg, "Item out of stock "
        else:
            product_page.add_to_wishlist()
            confirmation_msg = product_page.get_wishlist_msg()
            assert f"{product_name} has been added to your Wish List" in confirmation_msg

    # select random item from men's category using filter options and add to cart
    def test_add_product_men(self):

        menu = Menu(self.driver)
        menu.select_category('Men')
        filter_option, product_list = menu.select_submenu_men()
        self.wait_for_visibility_of_element(filter_option.filter_options)

        # select an item using the filters on left of products page and add to cart
        filter_option.select_filter_size()
        self.wait_for_visibility_of_element(filter_option.material)
        filter_option.select_filter_material()

        # check if price filter is visible
        price = self.wait_for_visibility_of_element(filter_option.price)
        if price:
            filter_option.select_filter_price()

        # wait for the products to load based on filters selected
        self.wait_for_visibility_of_element(product_list.men_products_wrapper)

        # select product from the results and fetch product name
        product_list.select_product_men()
        product_name = product_list.get_product_name()

        # select the colour, add product and assert
        product_list.select_colour()
        product_list.add_product()
        success_message = self.wait_for_visibility_of_element(product_list.success_msg).text
        assert product_name in success_message

    # select from other menu options
    def test_add_to_wishlist(self):
        menu = Menu(self.driver)
        product_list = menu.select_submenu_other()
        self.wait_for_visibility_of_element(product_list.title)

        # select random item from the page and add to wishlist
        product_name = product_list.select_product_other()
        product_list.add_product_to_wishlist()
        success_text = self.wait_for_visibility_of_element(product_list.success_msg).text
        assert product_name in success_text

    # checkout
    def test_checkout(self, get_data):
        checkout = CheckOut(self.driver)
        checkout.get_shopping_cart()
        checkout.proceed_to_checkout()
        text = 'Shipping Address'
        self.wait_for_text_presence(checkout.address, text)

        # enter the shipping address
        checkout.enter_street_1(get_data["street1"])
        checkout.enter_street_2(get_data["street2"])
        checkout.enter_city(get_data["city"])
        checkout.select_country()
        checkout.select_state()
        checkout.enter_zipcode(get_data["zipcode"])
        checkout.enter_phone(get_data["phone"])

        # select the shipping method and make payment
        checkout.select_shipping_method()
        payment_title = "Payment Method"
        self.wait_for_text_presence(checkout.payment_page, payment_title)
        self.wait_for_element_to_be_clickable(checkout.checkout_button)
        checkout.click_checkout()

        order_number = self.wait_for_visibility_of_element(checkout.order_number).text
        success_msg = checkout.get_success_msg()
        assert order_number in success_msg

    # logout
    def test_logout(self):
        logout = Logout(self.driver)
        logout.click_actions()
        logout.click_logout()

    @pytest.fixture(params=E2ETestData.shipping_address)
    def get_data(self, request):
        return request.param
