from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.config import *


def test_remove_product(setup):

    driver = setup

    driver.get(URL)

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(driver)

    inventory.add_product()

    inventory.remove_product()

    assert driver.find_element(*inventory.btn_add_backpack).is_displayed()