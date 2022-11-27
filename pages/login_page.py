from selenium.webdriver.common.by import By


from .dashboard_page import DashboardPage
from .base_page import BasePage

class LoginPage(BasePage):
    EMAIL_INPUT_BOX = (By.CSS_SELECTOR, "input[data-cy='email']")
    PWD_INPUT_BOX = (By.CSS_SELECTOR, 'input[data-cy="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button[data-cy="submit"]')

    def __init__(self, driver) -> None:
        super().__init__(driver)
    
    def open_url(self, url):
        self.driver.get(url)
        self.sl.waits.wait_until_element_is_visible(self.EMAIL_INPUT_BOX)
        
        return self

    def input_email(self, email):
        self.sl.waits.wait_until_element_is_enabled(self.EMAIL_INPUT_BOX)
        element = self.sl.base.find_element(self.EMAIL_INPUT_BOX)
        element.send_keys(email)

        return self

    def input_password(self, pwd):
        element = self.driver.find_element(*self.PWD_INPUT_BOX)
        element.send_keys(pwd)

        return self

    def submit(self):
        self.sl.waits.wait_until_element_is_enabled(self.LOGIN_BUTTON)
        element = self.sl.base.find_element(self.LOGIN_BUTTON)
        element.click()

        self.sl.waits.wait_until_page_is_loaded()
        self.sl.waits.wait_until_page_contains("Dashboard")
        
        return DashboardPage(self.driver)

