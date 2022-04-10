import pytest
from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ChromeOptions, Chrome
from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver

opts = ChromeOptions()
opts.add_experimental_option("detach", True)


@pytest.fixture(scope="class")
def setup(request):
    opts = ChromeOptions()
    opts.add_experimental_option("detach", True)
    # driver = Chrome(chrome_options=opts)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    driver.maximize_window()
    driver.implicitly_wait(8)
    driver.get("https://gifbuz.com/")
    request.cls.driver = driver
    yield
    driver.close()



