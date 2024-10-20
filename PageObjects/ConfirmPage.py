from selenium.webdriver.common.by import By


class Confirmpage:

    def __init__(self,driver):
        self.driver = driver

    CountrySelect = (By.ID,"country")



    def selectcountry(self):
        return self.driver.find_element(*Confirmpage.CountrySelect)