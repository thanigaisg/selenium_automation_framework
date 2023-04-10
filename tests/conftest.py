import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as MSEdgeService

driver = None
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope='class')
def setup(request):

    global driver
    browser = request.config.getoption("browser_name")

    if browser == "chrome":
        serv_obj = ChromeService("webdrivers\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    elif browser == "firefox":
        serv_obj = FirefoxService("webdrivers\\geckodriver_v0_33_0-win32\\geckodriver.exe")
        driver = webdriver.Firefox(service=serv_obj)
    elif browser == "edge":
        serv_obj = MSEdgeService("webdrivers\\edgedriver_win64\\msedgedriver.exe")
        driver = webdriver.Edge(service=serv_obj)
    else:
        serv_obj = ChromeService("webdrivers\\chromedriver_win32\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)

    driver.implicitly_wait(2)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver = driver

    yield

    driver.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)
