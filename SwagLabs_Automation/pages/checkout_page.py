from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    txt_firstname = (By.ID, "first-name")
    txt_lastname = (By.ID, "last-name")
    txt_zip = (By.ID, "postal-code")
    btn_continue = (By.ID, "continue")
    btn_finish = (By.ID, "finish")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_details(self, firstname, lastname, zipcode):
        self.wait.until(
            EC.visibility_of_element_located(self.txt_firstname)
        ).send_keys(firstname)

        self.driver.find_element(*self.txt_lastname).send_keys(lastname)

        self.driver.find_element(*self.txt_zip).send_keys(zipcode)

    def continue_checkout(self):
        self.driver.find_element(*self.btn_continue).click()

    def finish_order(self):
        self.wait.until(
            EC.element_to_be_clickable(self.btn_finish)
        ).click()