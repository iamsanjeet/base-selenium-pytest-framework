from .waits import Waits
from .selenium_base import SeleniumBase

class SeleniumLibrary:
    def __init__(self, driver) -> None:
        self.base = SeleniumBase(driver)
        self.waits = Waits(driver)
