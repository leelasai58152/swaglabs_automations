from pages.login_page import LoginPage
from utils.config import *


def test_invalid_login(setup):

    driver = setup

    driver.get(URL)

    login = LoginPage(driver)

    login.login(
        "standard_user",
        "wrongpassword"
    )

    assert "inventory" not in driver.current_url