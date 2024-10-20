from selenium.webdriver.common.by import By
from selenium import webdriver

from PageObjects.CheckoutPage import checkoutpage


class Homepage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT,"Shop")

    # TestCase-2
    name = (By.CSS_SELECTOR,"[name ='name']")
    email = (By.NAME,"email")
    id = (By.ID,"exampleCheck1")
    submit = (By.XPATH,"//input[@value='Submit']")
    successMessage = (By.XPATH,"//div[@class = 'alert alert-success alert-dismissible']")
    Gender = (By.ID,"exampleFormControlSelect1")
    def shopItems(self):
        self.driver.find_element(*Homepage.shop).click()
        # Class variable is called with class name and it is the variable which is present inside the class but outside the method.
        # When we put star with class name then it treats variable as a tuple.
        checkout_object = checkoutpage(self.driver)
        return checkout_object

    def getName(self):
        return self.driver.find_element(*Homepage.name)

    def getEmail(self):
        return self.driver.find_element(*Homepage.email)
    def getId(self):
        return self.driver.find_element(*Homepage.id)

    def submitform(self):
        return self.driver.find_element(*Homepage.submit)

    def getSuccessMessage(self):
        return self.driver.find_element(*Homepage.successMessage)

    def getGender(self):
        return self.driver.find_element(*Homepage.Gender)
