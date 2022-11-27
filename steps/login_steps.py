
# import 3rd party libraries
import pytest

# import pages library
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

# import logger
from lib.utils.logger import getLogger
logger = getLogger(__name__)

class LoginSteps:
    def __init__(self, driver) -> None:
        self.driver = driver

    def login_with_valid_credential(self, url, email, pwd):
        LoginPage(self.driver) \
            .open_url(url) \
            .input_email(email) \
            .input_password(pwd) \
            .submit()
    
    def assert_dashboard_page_landing(self):
        dashboard_page_obj = DashboardPage(self.driver)

        # assert on url
        url = dashboard_page_obj.get_url()
        logger.info(f"Dashboard page url is - {url}")

        assert '/dashboard' in url

        # assert on header text
        header = dashboard_page_obj.get_header()
        logger.info(f"Dashboard page header is - {header}")
        assert 'Dashboard' == header

    def login_with_invalid_credential(self):
        pass
