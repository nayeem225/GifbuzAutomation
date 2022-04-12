from selenium.webdriver.common.by import By


class LogInPage:

    def __init__(self, driver):
        self.driver = driver

    emailID = (By.CSS_SELECTOR, "#lEmail")
    password = (By.CSS_SELECTOR, "#password")
    enterButton = (By.XPATH, "//button[contains(text(),'Log In')]")
    blankEmailMessage = (By.XPATH, "//p[contains(text(),'Enter e-mail address')]")
    blankPasswordMessage = (By.XPATH, "//span[contains(text(),'Password should no be empty!')]")

    def EmailId(self):
        return self.driver.find_element(*LogInPage.emailID)

    def Password(self):
        return self.driver.find_element(*LogInPage.password)

    def EnterButton(self):
        return self.driver.find_element(*LogInPage.enterButton)

    def BlankEmailMessage(self):
        return self.driver.find_element(*LogInPage.blankEmailMessage)

    def BlankPasswordMessage(self):
        return self.driver.find_element(*LogInPage.blankPasswordMessage)