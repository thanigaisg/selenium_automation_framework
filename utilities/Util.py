import inspect
import logging

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')
class Util:

    def verifyPresenceElements(self, webelements):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(webelements))

    def selectOptionbytext(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    def getLogger(self):

        loggername = inspect.stack()[1][3]
        log = logging.getLogger(loggername)

        filehandler = logging.FileHandler("logfile.log")

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        filehandler.setFormatter(formatter)

        log.addHandler(filehandler)  # filehandler object

        log.setLevel(logging.DEBUG)

        return log