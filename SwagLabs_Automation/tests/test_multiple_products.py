from pages.login_page import LoginPage
from utils.config import *


def test_multiple_products(setup):

    driver = setup

    driver.get(URL)

    login = LoginPage(driver)

    login.login(USERNAME, PASSWORD)

    products = [

        "add-to-cart-sauce-labs-backpack",

        "add-to-cart-sauce-labs-bike-light",

        "add-to-cart-sauce-labs-bolt-t-shirt"

    ]

    for product in products:

        driver.find_element("id", product).click()

    assert driver.find_element(
        "class name",
        "shopping_cart_badge"
    ).text == "3"
    
    
'''
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from utils.config import *

def test_multiple_products(setup):

    driver = setup
    driver.get(URL)

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    # Backpack Add
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # Bike Light Add
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    # Bolt T-Shirt Add
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    # Cart Badge Check
    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

    assert cart_count == "3"'''