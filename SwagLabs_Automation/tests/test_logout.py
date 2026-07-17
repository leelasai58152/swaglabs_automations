from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from pages.logout_page import LogoutPage
from utils.config import *


def test_logout(setup):

    driver = setup

    driver.get(URL)

    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    menu = MenuPage(driver)
    menu.open_menu()

    logout = LogoutPage(driver)
    logout.logout()

    WebDriverWait(driver, 10).until(
        EC.url_to_be(URL)
    )

    assert driver.current_url == URL