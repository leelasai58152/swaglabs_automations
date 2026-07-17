from pages.login_page import LoginPage
from utils.config import *


def test_login(setup):

    driver = setup

    driver.get(URL)

    login = LoginPage(driver)

    login.login(USERNAME, PASSWORD)

    assert "inventory" in driver.current_url