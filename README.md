This is a Selenium-based test automation suite using Python and Pytest, designed to automate test cases for the demo online shopping website, LUMA.

Project Structure:

config: Contains configuration settings for the automation suite (credentials, URLs, etc.). The sensitive information is stored in the config.ini file, which is excluded from version control.

page_objects: Implements the Page Object Model (POM) design pattern. Each page of the application is represented by a class encapsulating web elements and actions related to that page.

checkout.py, create_account.py, login.py, logout.py, etc.
test_data: Stores test data required for test cases such as user credentials and account creation data.

tests: Contains the test scripts that drive the automation. The tests are written using Pytest framework.

test_add_products.py, test_delete_products.py, test_new_user_create_account.py, etc.
utilities: Includes utility classes and methods used across the framework.

base_class.py handles the setup and teardown methods for the browser, along with common methods needed in tests.

Setup:

Prerequisites
Python 3.12 or higher installed
Google Chrome browser installed
Required Python packages:
pytest
selenium

Tests:

New User Tests
1. Account Creation
Valid Account Creation: Tests creating an account with valid data.
Invalid Account Creation: Tests various negative scenarios such as missing fields, mismatched passwords, etc.
2. End-to-End Workflow: Completes the user journey from account creation to purchasing products.

Existing User Tests
1. Add Multiple Products to Cart: Adds multiple items to the cart and verifies the correct products are added.
2. Delete product: Delete product from cart and verifies the updated quantity and subtotal price


Design Pattern
This project follows the Page Object Model (POM) to enhance test maintenance and reusability. Each page of the application is represented by a class, and the elements on the page are encapsulated as methods within that class. This allows for separation of test scripts from the actual UI interactions, making the code more maintainable.

Note
This project is still a Work In Progress. Additional test cases and enhancements will be added as the development of automation scripts continues.