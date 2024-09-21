from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from random import choice
from page_objects.filter_options import FilterOptions
from page_objects.other_products import OtherCategory
from page_objects.products_list import ProductList


class Menu:
    women_submenu_level_1 = (By.CSS_SELECTOR, ".level0.nav-2.category-item ul li.level1")
    women_submenu_level_2 = (By.CSS_SELECTOR, "ul li.level2")
    men_submenu_level_1 = (By.CSS_SELECTOR, ".level0.nav-3.category-item ul li.level1")
    men_submenu_level_2 = (By.CSS_SELECTOR, "ul li.level2")
    gear = (By.CSS_SELECTOR, "li.level0.nav-4.category-item")
    gear_submenu = (By.CSS_SELECTOR, "ul li.level1")
    submenu_text = (By.CSS_SELECTOR, "span")

    def __init__(self, driver):
        self.driver = driver

    def select_category(self, category):
        category = (By.LINK_TEXT, category)
        category_element = self.driver.find_element(*category)
        action = ActionChains(self.driver)
        action.move_to_element(category_element).perform()

    def select_submenu_women(self):
        # select submenu at level 1
        women_submenu_level_1 = self.driver.find_elements(*Menu.women_submenu_level_1)
        select_submenu_level_1 = choice(women_submenu_level_1)
        action = ActionChains(self.driver)
        action.move_to_element(select_submenu_level_1).perform()

        # select submenu at level 2
        women_submenu_level_2 = select_submenu_level_1.find_elements(*Menu.women_submenu_level_2)
        select_submenu_level_2 = choice(women_submenu_level_2)
        select_submenu_level_2.click()

        # create and return ProductList instance
        product_list = ProductList(self.driver)
        return product_list

    def select_submenu_men(self):
        # select submenu at level 1
        men_submenu_level_1_element = self.driver.find_elements(*Menu.men_submenu_level_1)
        select_submenu_level_1 = choice(men_submenu_level_1_element)
        action = ActionChains(self.driver)
        action.move_to_element(select_submenu_level_1).perform()

        # select submenu at level 2
        men_submenu_level_2_element = select_submenu_level_1.find_elements(*Menu.men_submenu_level_2)
        select_submenu_level_2 = choice(men_submenu_level_2_element)
        select_submenu_level_2.click()

        # create and return FilterOptions and ProductList instances
        filter_option = FilterOptions(self.driver)
        product_list = ProductList(self.driver)
        return filter_option, product_list

    def select_submenu_other(self):
        gear_element = self.driver.find_element(*Menu.gear)
        action = ActionChains(self.driver)
        action.move_to_element(gear_element).perform()
        gear_submenu_element = gear_element.find_elements(*Menu.gear_submenu)
        select_submenu = choice(gear_submenu_element)
        select_submenu.click()
        product_list = OtherCategory(self.driver)
        return product_list
