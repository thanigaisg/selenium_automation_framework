from pageObjects.HomePage import HomePage
from utilities.Util import Util
import time


class Test_E2E(Util):

    def test_e2e(self):

        log = self.getLogger()

        home = HomePage(self.driver)
        checkout = home.shopItems()

        log.info("Getting all the card titles")
        products = checkout.getCardTitles()

        for product in products:
            title_text = checkout.getProductName(product).text.lower()
            log.debug(title_text)
            if "blackberry" in title_text:
                checkout.addToCart(product).click()
                break

        log.info("Checking out the Blackberry Product")
        checkout.getCheckout().click()

        confirm = checkout.getConfirmCheckout()

        log.info("Providing shipping country as India")
        countries = confirm.getCountrySuggestions("ind")
        for country in countries:
            country_name = confirm.getCountryName(country)
            if "india" in country_name.text.lower():
                country_name.click()
                break

        log.info("Confirming the Terms and Conditions")
        confirm.getTCCheckbox().click()

        log.info("Confirming the Purchase")
        confirm.getPurchaseBtn().click()

        alert_msg = confirm.getAlertMessage().text
        assert "Success! Thank you!" in alert_msg
        log.info(alert_msg)

        time.sleep(2)
