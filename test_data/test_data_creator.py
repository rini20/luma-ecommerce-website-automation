from faker import Faker
import json

fake = Faker()
'''
create_account_dataset = dict(test_valid_data={
    'firstname': fake.first_name(),
    'lastname': fake.last_name(),
    'email_address': fake.email(),
    'password': fake.password(length=10, upper_case=True, lower_case=True, special_chars=True, digits=True),
    'phone': fake.phone_number(),
    'street_address': fake.street_address()
}, test_invalid_password={
    'firstname': fake.first_name(),
    'lastname': fake.last_name(),
    'email_address': fake.email(),
    'password': fake.password(length=8, upper_case=False, lower_case=True, special_chars=False, digits=True)
}, test_password_mismatch={
    'firstname': fake.first_name(),
    'lastname': fake.last_name(),
    'email_address': fake.email(),
    'password': fake.password(length=8, upper_case=True, lower_case=True, special_chars=False, digits=True),
    'password-confirmation': fake.password(length=9)
}, test_incomplete_data={
    'firstname': fake.first_name(),
    'lastname': fake.last_name(),
    'email_address': '',
    'password': fake.password(length=10, upper_case=True, lower_case=True, special_chars=True, digits=True)
})

json_data = json.dumps(create_account_dataset, indent=4)

with open("create_account_testdata", "w") as file:
    file.write(json_data)
'''

address_dataset = [
    {
        'street1': fake.street(),
        'street2': fake.secondary_address(),
        'city': fake.city(),
        'zipcode': fake.zipcode(),
        'phone': fake.phone_number()
    }
]

json_data = json.dumps(address_dataset, indent=4)

with open("E2E_test_data", "w") as file:
    file.write(json_data)