import time

import pytest

from pageObjects.HomePage import HomePage
from testdata.HomePageData import HomePageData
from utilities.Util import Util


class TestHomePage(Util):

    def test_formSubmissiontupple(self, getData):

        log = self.getLogger()

        homepage = HomePage(self.driver)

        log.debug(f"Providing Name as {getData[0]}")
        homepage.getName().send_keys(getData[0])

        log.debug(f"Providing Email as {getData[1]}")
        homepage.getEmail().send_keys(getData[1])

        log.debug("Providing Password")
        homepage.getPassword().send_keys(getData[2])

        homepage.getCheckbox().click()
        homepage.getRadiobtn().click()

        log.debug(f"Providing Gender as {getData[3]}")
        self.selectOptionbytext(homepage.getGender(), getData[3])

        log.debug(f"Proving DOB as {getData[4]}")
        homepage.getBday().send_keys(getData[4])
        homepage.getSubmitBtn().click()

        assert "Success!" in homepage.getAlert().text
        time.sleep(5)

        self.driver.refresh()

    def test_formSubmissiondict(self, getDataDict):

        log = self.getLogger()
        homepage = HomePage(self.driver)

        log.debug(f"Providing Name as {getDataDict['Name']}")
        homepage.getName().send_keys(getDataDict['Name'])

        log.debug(f"Providing Email as {getDataDict['E-Mail']}")
        homepage.getEmail().send_keys(getDataDict['E-Mail'])

        log.debug(f"Providing Password")
        homepage.getPassword().send_keys(getDataDict['Password'])
        homepage.getCheckbox().click()
        homepage.getRadiobtn().click()

        log.debug(f"Providing Gender as {getDataDict['Gender']}")
        self.selectOptionbytext(homepage.getGender(), getDataDict['Gender'])

        log.debug(f"Providing DOB as {getDataDict['DOB']}")
        homepage.getBday().send_keys(getDataDict['DOB'])
        homepage.getSubmitBtn().click()

        assert "Success!" in homepage.getAlert().text
        time.sleep(5)

        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_homepage_tup)
    def getData(self, request):
        return request.param

    @pytest.fixture(params=HomePageData.getTestData("testcase2", "testcase4", "testcase7"))
    def getDataDict(self, request):
        return request.param
