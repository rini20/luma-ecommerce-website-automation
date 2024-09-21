from page_objects.logout import Logout
from utilities.base_class import BaseClass
from page_objects.login import Login
from page_objects.menu import Menu
from test_data import test_users_credentials as UC


class TestAdd(BaseClass):

    def test_login(self):
        login = Login(self.driver)
        login.click_sign_in()
        login.enter_email(UC.existing_username)
        login.enter_password(UC.existing_password)
        login.sign_in()
        element = self.wait_for_text_presence(login.welcome_msg, 'Welcome')
        assert element

    def test_add_products(self):
        for _ in range(2):
            menu = Menu(self.driver)
            menu.select_category('Women')
            product_list = menu.select_submenu_women()
            product = product_list.select_product_women()
            product.browse_product_images()
            product_name = product.get_product_name()
            product.browse_product_images()
            product.select_size()
            product.select_colour()
            product.enter_quantity(1)
            product.add_product()
            assert product_name in product.get_add_msg()

    def test_logout(self):
        logout = Logout(self.driver)
        logout.click_actions()
        logout.click_logout()