import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from PageObjects.CheckoutPage import checkoutpage
from PageObjects.ConfirmPage import Confirmpage
from PageObjects.HomePage import Homepage
from Utilities.baseclass import BaseClass


# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):
        self.driver.implicitly_wait(4)
        homepage_object = Homepage(self.driver)
        checkout_object = homepage_object.shopItems()
        # self.driver.find_element(By.LINK_TEXT, "Shop").click()
        # Or self.driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click() This is an example of regular expression.


        productlist = checkout_object.CheckOut()
        # productlist = self.driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        for product in productlist:
            ProductName = product.find_element(By.XPATH, "div/h4/a").text
            if ProductName == "Blackberry":
                checkout_object.ProductSelect().click()
                # product.find_element(By.XPATH, "div/button").click()
                # product.find_element(By.CSS_SELECTOR,".card-footer button")

        self.driver.implicitly_wait(4)
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()  # regular expression

        # self.driver.find_element(By.XPATH, "//tbody/tr[3]/td[5]").click()
        Confirmpage_object= checkout_object.checkout2func()
        print(Confirmpage_object)
        # self.driver.find_element(By.ID, "country").send_keys("Ind")
        # Confirmpage_object.CountrySelect().send_Keys("Ind")
        Confirmpage_object.selectcountry().send_keys("Ind")

          # Check what this prints

        # Important to understand this concept...
        # wait = WebDriverWait(self.driver, 10)
        # from selenium.webdriver.support import expected_conditions

        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.verifyLinkPresence("India")

        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class = 'checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type = 'submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert "Success! Thank you!" in successText


        # It is a small project to understand the basics of Selenium. Thankyou!
