from typing import Optional, Union
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebElement
from selenium.webdriver.common.by import By


class SeleniumBase:
    def __init__(self, driver) -> None:
        self.driver = driver
    
    def find_element(self, locator: Union[tuple, WebElement]):
        if self._is_webelement(locator):
            return locator

        return self.driver.find_element(*locator)

    def escape_xpath_value(self, value: str):
        value = str(value)
        if '"' in value and "'" in value:
            parts_wo_apos = value.split("'")
            escaped = "', \"'\", '".join(parts_wo_apos)
            return f"concat('{escaped}')"
        if "'" in value:
            return f'"{value}"'
        return f"'{value}'"

    def is_visible(self, locator) -> bool:
        element = self.find_element(locator)
        return element.is_displayed() if element else None

    def is_text_present(self, text: str):
        locator = (By.XPATH, f"//*[contains(., {self.escape_xpath_value(text)})]")
        return self.find_element(locator) is not None

    def is_element_enabled(self, locator: str, tag: Optional[str] = None) -> bool:
        element = self.find_element(locator)
        return element.is_enabled() and element.get_attribute("readonly") is None
    
    def get_timeout(self):
        return 30
    
    def _is_webelement(self, element):
        # Hook for unit tests
        return isinstance(element, (WebElement, EventFiringWebElement))