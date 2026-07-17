from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    btn_add_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    btn_remove_backpack = (By.ID, "remove-sauce-labs-backpack")
    btn_cart = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_product(self):
        self.wait.until(
            EC.element_to_be_clickable(self.btn_add_backpack)
        ).click()

    def remove_product(self):
        self.wait.until(
            EC.element_to_be_clickable(self.btn_remove_backpack)
        ).click()

    def open_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.btn_cart)
        ).click()