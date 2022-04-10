import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        self.driver.get("https://gifbuz.com/")
        print("Gifbuz Login Test : Empty Mail and Empty Password")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,
                            value="//body[1]/div[1]/div[1]/div[3]/div[2]/button[1]").click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,
                            value="//body[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]").click()

        # login
        self.driver.find_element(by=By.XPATH,
                            value="//input[@id='lEmail']").send_keys("")
        time.sleep(2)

        # password
        self.driver.find_element(by=By.CSS_SELECTOR,
                            value="#password").send_keys("")
        self.driver.find_element(by=By.XPATH, value="//button[contains(text(),'Log In')]").click()
        time.sleep(2)

        blankEmailMessage = self.driver.find_element(by=By.XPATH,
                                                value="//p[contains(text(),'Enter e-mail address')]").text
        print('Bllank Email Message:', blankEmailMessage)

        blankPasswordMessage = self.driver.find_element(by=By.XPATH,
                                                   value="//span[contains(text(),'Password should no be empty!')]").text
        print('Bllank Email Message:', blankPasswordMessage)

        assert "Enter e-mail address" == blankEmailMessage, "Dhur mia, Email Dite ke koice"
        print(" Thanks for not giving any Email ")

        assert "Password should no be empty!" == blankPasswordMessage, "Password Dite bolce ke ?"
        print("Thanks for not giving any password")

