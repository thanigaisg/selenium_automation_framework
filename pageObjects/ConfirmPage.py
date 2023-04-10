from selenium.webdriver.common.by import By
from utilities.Util import Util


class ConfirmPage(Util):

    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    suggestions = (By.CSS_SELECTOR, ".suggestions")
    name = (By.XPATH, "ul/li/a")
    checkbox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    purchase = (By.CSS_SELECTOR, "input[class~=btn-success]")
    alert = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def getCountrySuggestions(self, country_kw):
        self.driver.find_element(*ConfirmPage.country).send_keys(country_kw)

        self.verifyPresenceElements(ConfirmPage.suggestions)

        return self.driver.find_elements(*ConfirmPage.suggestions)

    def getCountryName(self, country):
        return country.find_element(*ConfirmPage.name)

    def getTCCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getPurchaseBtn(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def getAlertMessage(self):
        return self.driver.find_element(*ConfirmPage.alert)

