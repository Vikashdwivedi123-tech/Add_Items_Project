from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import Confirmpage


class checkoutpage:

    def __init__(self, driver):
        self.driver = driver

    checkout = (By.XPATH, "//div[@class='card h-100']")
    productselect = (By.CSS_SELECTOR, ".card-footer button")
    checkout2 = (By.XPATH,"//tbody/tr[3]/td[5]")
    # CountrySelect = (By.ID, "country")

    def CheckOut(self):
        return self.driver.find_elements(*checkoutpage.checkout)

    def ProductSelect(self): #Checkoutitem
        return self.driver.find_element(*checkoutpage.productselect)

    def checkout2func(self):
        self.driver.find_element(*checkoutpage.checkout2).click()
        Confirmpage_object = Confirmpage(self.driver)
        return Confirmpage_object

