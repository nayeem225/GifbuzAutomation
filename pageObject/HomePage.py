from selenium.webdriver.common.by import By
from webdriver_manager import driver


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    Login = (By.XPATH, "//a[@class='btn btn-primary'][normalize-space()='Login']")
    ConfirmButton =(By.CSS_SELECTOR, "#rcc-confirm-button")

    def LoginInside(self):
        return self.driver.find_element(*HomePage.Login)

    def confirmButton(self):
        return self.driver.find_element(*HomePage.ConfirmButton)
