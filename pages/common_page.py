from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium.webdriver.chrome.webdriver import WebDriver

from lib.utils.logger import getLogger
logger = getLogger(__name__)


class CommonPage(BasePage):

    def __init__(self, driver) -> None:
        super().__init__(driver)
    
    def get_url(self):
        return self.driver.current_url