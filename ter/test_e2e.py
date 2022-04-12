import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObject.HomePage import HomePage
from pageObject.LoginPage import LogInPage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        homePage = HomePage(self.driver)
        loginPage = LogInPage(self.driver)

        print("Gifbuz Login Test : Empty Mail and Empty Password")
        time.sleep(2)
        #caokies
        homePage.confirmButton().click()
        time.sleep(5)
        #Login Button Click
        homePage.LoginInside().click()
        time.sleep(5)

        # Email Id
        loginPage.EmailId().send_keys("")
        time.sleep(2)

        # Password
        loginPage.Password().send_keys("")
        # EnterButton
        loginPage.EnterButton().click()
        # time.sleep(2)

        blankEmailMessage = loginPage.BlankEmailMessage().text
        print('Bllank Email Message:', blankEmailMessage)

        blankPasswordMessage = loginPage.BlankPasswordMessage().text
        print('Bllank Email Message:', blankPasswordMessage)

        assert "Enter e-mail address" == blankEmailMessage, "Dhur mia, Email Dite ke koice"
        print(" Thanks for not giving any Email ")

        assert "Password should no be empty!" == blankPasswordMessage, "Password Dite bolce ke ?"
        print("Thanks for not giving any password")
