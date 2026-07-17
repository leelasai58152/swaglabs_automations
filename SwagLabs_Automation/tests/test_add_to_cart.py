from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import *


def test_add_to_cart(setup):

    driver = setup

    driver.get(URL)

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(driver)
    inventory.add_product()

    assert driver.find_element(*inventory.btn_remove_backpack).is_displayed()