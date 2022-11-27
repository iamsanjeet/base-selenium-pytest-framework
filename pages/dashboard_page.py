from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver

from .base_page import BasePage
from .common_page import CommonPage

from lib.utils.logger import getLogger
logger = getLogger(__name__)

class DashboardPage(CommonPage):
    HEADER_TEXT = (By.CSS_SELECTOR, "h1[data-cy='dashboard']")

    def __init__(self, driver) -> None:
        super().__init__(driver)
    
    def get_header(self):
        webelement = self.sl.base.find_element(self.HEADER_TEXT)
        return webelement.text

    

