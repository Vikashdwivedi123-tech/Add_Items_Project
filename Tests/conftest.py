from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action = "store", default = "chrome" # key value concept to run the browser in terminal of your choice.
    )

@pytest.fixture(scope = "class")
def setup(request):
    browser_name = request.config.getoption("browser_name")
    if(browser_name == "chrome"):
        driver = webdriver.Chrome()
        # driver.implicitly_wait(5)

    elif(browser_name == "firefox"):
        driver = webdriver.Firefox()

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver
    yield   # It will execute when the execution of class is completed
    driver.close()



