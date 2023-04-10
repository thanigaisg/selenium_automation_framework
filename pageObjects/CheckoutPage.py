from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    productTitle = (By.CSS_SELECTOR, "div h4 a")
    addCart = (By.XPATH, "div/button")
    clickCheckout = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    confirmCheckout = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckoutPage.cardTitle)

    def getProductName(self, product):
        return product.find_element(*CheckoutPage.productTitle)

    def addToCart(self, product):
        return product.find_element(*CheckoutPage.addCart)

    def getCheckout(self):
        return self.driver.find_element(*CheckoutPage.clickCheckout)

    def getConfirmCheckout(self):
        self.driver.find_element(*CheckoutPage.confirmCheckout).click()
        return ConfirmPage(self.driver)