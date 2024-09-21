from selenium.webdriver.common.by import By
from test_data import test_users_credentials as UC


class CreateAccTestData:
    test_create_account_invalid_data = [
        {

            "firstname": "Jacob",
            "lastname": "George",
            "email_address": "andrewcastro@example.net",
            "password": "4d0l24bl",
            "password-confirmation": "4d0l24bl",
            "error_locator": (By.CSS_SELECTOR, "#password-error"),
            "error": "Minimum of different classes of characters in password is 3"
        },

        {

            "firstname": "Jennifer",
            "lastname": "Perkins",
            "email_address": "laurenbowen@example.com",
            "password": "Gcpe3dOd",
            "password-confirmation": "R+_5CyupA",
            "error_locator": (By.CSS_SELECTOR, "#password-confirmation-error"),
            "error": "same value again"
        },

        {

            "firstname": "William",
            "lastname": "Long",
            "email_address": "",
            "password": "1pIJ3uye@1",
            "password-confirmation": "1pIJ3uye@1",
            "error_locator": (By.ID, "email_address-error"),
            "error": "required field"
        }

    ]

    test_create_account_success = [
        {
            "firstname": "Michael",
            "lastname": "Green",
            "email_address": UC.username,
            "password": UC.password,
            "password-confirmation": UC.password
        }

    ]
