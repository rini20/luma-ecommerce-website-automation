from utilities.base_class import BaseClass
from page_objects.create_account import CreateAccount
from test_data.create_account_test_data import CreateAccTestData
import pytest

# Navigate to create new customer account page


class TestCreateAccount(BaseClass):

    def test_create_account_invalid_data(self, get_invalid_data):
        create_account = CreateAccount(self.driver)
        create_account.goto_create_account()
        create_account.enter_firstname(get_invalid_data["firstname"])
        create_account.enter_lastname(get_invalid_data["lastname"])
        create_account.enter_email(get_invalid_data["email_address"])
        create_account.enter_password(get_invalid_data["password"])
        create_account.reenter_password(get_invalid_data["password-confirmation"])
        create_account.submit()
        error_value = get_invalid_data["error"]
        error_locator = get_invalid_data["error_locator"]
        error = create_account.get_error_message(error_locator).text
        assert error_value in error

    def test_create_account_success(self, get_valid_data):
        create_account = CreateAccount(self.driver)
        create_account.enter_firstname(get_valid_data["firstname"])
        create_account.enter_lastname(get_valid_data["lastname"])
        create_account.enter_email(get_valid_data["email_address"])
        create_account.enter_password(get_valid_data["password"])
        create_account.reenter_password(get_valid_data["password-confirmation"])
        create_account.submit()
        account_title = self.wait_for_visibility_of_element(create_account.account_page_title)
        assert account_title.is_displayed()

    @pytest.fixture(params=CreateAccTestData.test_create_account_invalid_data)
    def get_invalid_data(self, request):
        return request.param

    @pytest.fixture(params=CreateAccTestData.test_create_account_success)
    def get_valid_data(self, request):
        return request.param



