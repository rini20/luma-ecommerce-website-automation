import configparser
import os


file_path = os.path.abspath('..')
config = configparser.ConfigParser()
config_path = os.path.join(file_path, "config", "config.ini")
# print(config_path)
config.read(config_path)
# print(config.sections())
try:
    new_username = config['credentials']['username']
    new_password = config['credentials']['password']
    existing_username = config['credentials']['test_username']
    existing_password = config['credentials']['test_password']
except KeyError:
    print("The credentials are missing in config file")

