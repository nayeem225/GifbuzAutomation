import pytest
from selenium import webdriver
# Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# Edge
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
# Firefox
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# process 1 import

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


# @pytest.fixture(scope="class")
#
# def setup(request):

# Process 1

# opts = ChromeOptions()
# opts.add_experimental_option("detach", True)
# # driver = Chrome(chrome_options=opts)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
# driver.maximize_window()
# driver.implicitly_wait(8)
# driver.get("https://gifbuz.com/")
# request.cls.driver = driver
# yield
# driver.close()

# process 2

# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://gifbuz.com/")
# driver.maximize_window()
# request.cls.driver = driver
# yield

# Process to run with all browser
# py.test --browser_name edge


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    elif browser_name == "edge":
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    driver.get("https://gifbuz.com/")
    driver.maximize_window()
    # driver.implicitly_wait(8)

    request.cls.driver = driver
    yield
    driver.close()
