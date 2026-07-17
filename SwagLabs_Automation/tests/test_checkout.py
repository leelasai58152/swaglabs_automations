from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.config import *


def test_checkout(setup):

    driver = setup

    driver.get(URL)

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    inventory = InventoryPage(driver)
    inventory.add_product()
    inventory.open_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)

    checkout.enter_details(
        "Leela",
        "Sai",
        "516360"
    )

    checkout.continue_checkout()

    checkout.finish_order()

    assert "checkout-complete" in driver.current_url