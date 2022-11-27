
from lib.selenium import SeleniumLibrary
from selenium.webdriver.chrome.webdriver import WebDriver

class BasePage:
    def __init__(self, driver) -> None:
        self.driver: WebDriver = driver
        self.sl = SeleniumLibrary(driver)
        