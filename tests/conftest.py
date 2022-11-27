import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options as ChOptions
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.ie.options import Options as IEOptions
from py.xml import html
import os
from datetime import datetime
from selenium.webdriver.support.events import EventFiringWebDriver

class DriverInitializer:
    def __init__(self, name="chrome") -> None:
        self.name = name
    
    def initialize(self):
        options = self._initialize_options()
        driver: WebDriver = self._initialize_driver(options)

        return driver

    def _initialize_options(self):
        if self.is_chrome():
            options = ChOptions()
        
        if self.is_firefox():
            options = FFOptions()
        
        if self.is_ie():
            options = IEOptions()
        
        if self.is_headless():
            options.add_argument('--headless')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-gpu')
        
        return options

    def _initialize_driver(self, options):
        if self.is_chrome():
            driver = webdriver.Chrome(options=options)
        
        if self.is_firefox():
            driver = webdriver.Firefox(options=options)
        
        if self.is_ie():
            driver = webdriver.Ie(options=options)
        
        return driver
  
    def is_chrome(self):
        return self.name in ['chrome', 'ch', 'headlesschrome']

    def is_firefox(self):
        return self.name in ['firefox', 'ff', 'headlessfirefox']

    def is_ie(self):
        return self.name in ['ie', 'headlessie']

    def is_headless(self):
        return 'headless' in self.name

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://aaaaaaaaanightly.eng.macrometa.io/")
    parser.addoption("--results", action="store", default="results/")

@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="class")
def init_driver(request):
    browser = request.config.getoption("--browser")
    driver_initializer = DriverInitializer(browser)
    driver = driver_initializer.initialize()
    driver.implicitly_wait(30)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()

def pytest_html_report_title(report):
    report.title = "C8 GUI Automation Report"

def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("foo: bar")])

def pytest_configure(config):
    config._metadata['URL'] = config.getoption("--url")
    config._metadata['Browser'] = config.getoption("--browser")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    timestamp = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, "extra", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        # check if test failed
        if (report.skipped and xfail) or (report.failed and not xfail):
            results_dir = item.config.getoption("--results")
            screen_shot_path = os.path.join(os.getcwd(), results_dir, f"{item.name}-{timestamp}.png" )
            driver_fixture = item.funcargs['request']
            driver_fixture.cls.driver.save_screenshot(screen_shot_path)
            # only add additional html on failure
            # extra.append(pytest_html.extras.html('<div style="background:orange;">Additional HTML</div>'))
            extra.append(pytest_html.extras.image(screen_shot_path))

        report.extra = extra