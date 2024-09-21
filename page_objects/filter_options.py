from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import choice


class FilterOptions:
    filter_options = (By.CLASS_NAME, "block-content.filter-content")
    size = (By.XPATH, "//div[@class='filter-options-title' and text()='Size']")
    size_content = (By.XPATH, "following-sibling::div[@class='filter-options-content']//a//div")
    material = (By.XPATH, "//div[@class='filter-options-title' and text()='Material']")
    material_content = (By.XPATH, "following-sibling::div[@class='filter-options-content' and @aria-hidden='false']//ol//li")
    price = (By.XPATH, "//div[@class='filter-options-title' and text()='Price']")
    price_content = (By.XPATH, "following-sibling::div[@class='filter-options-content']//ol//li")

    def __init__(self, driver):
        self.driver = driver

    def select_filter_size(self):
        # select size from the size filter options
        size_element = self.driver.find_element(*FilterOptions.size)
        size_element.click()
        size_content_element = size_element.find_elements(*FilterOptions.size_content)
        choice(size_content_element).click()

    def select_filter_material(self):
        # wait for products page to be loaded after size selection
        # material_element = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(*FilterOptions.material))
        material_element = self.driver.find_element(*FilterOptions.material)
        material_element.click()

        # select material from the material filter options
        material_content_element = material_element.find_elements(*FilterOptions.material_content)
        choice(material_content_element).click()

    def select_filter_price(self):
        # select price range if price option is available
        price_element = self.driver.find_element(*FilterOptions.price)
        price_element.click()
        price_content_element = price_element.find_elements(*FilterOptions.price_content)
        choice(price_content_element).click()





