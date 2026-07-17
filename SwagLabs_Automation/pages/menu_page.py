from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage:

    btn_menu = (By.ID, "react-burger-menu-btn")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_menu(self):
        self.wait.until(
            EC.element_to_be_clickable(self.btn_menu)
        ).click()