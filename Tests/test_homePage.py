import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from PageObjects.HomePage import Homepage
from TestData.Homepagedata import HomePageData
from Utilities.baseclass import BaseClass
import pytest

class TestHomePage(BaseClass):

    def test_formSubmission(self,getData):



        # driver = webdriver.Chrome()
        # driver.get("https://rahulshettyacademy.com/angularpractice")
        # driver.maximize_window()

        # Above three lines comes in conftest.py file.
        log = self.getLogger()
        # driver.find_element_by_css_selector("[name ='name']").send_keys("Rahul")
        homePage = Homepage(self.driver)
        log.info("first name is "+getData["firstname"])

        homePage.getName().send_keys(getData["firstname"])

        # driver.find_element_by_name("email").send_keys("shetty")
        homePage.getEmail().send_keys(getData["lastname"])

        # driver.find_element_by_id("exampleCheck1").click()
        homePage.getId().click()

        # sel = Select(homePage.getGender())
        # sel.Select_by_visible_text("Male")
        self.selectOptionByText(homePage.getGender(),getData["gender"]) #Utility

        # driver.find_element_by_xpath("//input[@value='Submit']").click()
        homePage.submitform().click()


        # alerText = driver.find_element_by_css_selector("[class = 'alert-success']").text
        alerText = homePage.getSuccessMessage().text
        restMessage = "The Form has been submitted successfully!."
        # assert ("success" in alerText)
        assert alerText == f"×\nSuccess! {restMessage}" # Known as fstring..
        # csv = "2024"
        # alertMessage = f"Copyright © {csv} Venera Technologies Inc. All rights reserved."
        self.driver.refresh()

    @pytest.fixture(params = HomePageData.getExcelTestData("TestCase 2"))
    def getData(self, request):
        return request.param
