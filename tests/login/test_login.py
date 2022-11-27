
import pytest

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

from steps.login_steps import LoginSteps

from lib.utils.logger import getLogger

logger = getLogger(__name__)

from selenium import webdriver

@pytest.mark.sanity
@pytest.mark.usefixtures('init_driver')
class TestLogin:

    #
    # Example: To demonstrate page object model, fluent iterface and pytest markers
    #
    @pytest.mark.p0
    @pytest.mark.streams
    def test_successfull_login_tenant(self, base_url):
        logger.info("2222222222222222222running:::::::::::::test_successfull_login")
        LoginPage(self.driver) \
            .open_url(base_url) \
            .input_email('sanjeet.singh@macrometa.com') \
            .input_password("Macrometa123!@#") \
            .submit()
    #
    # Example: To demonstrate page object model, fluent iterface and pytest markers
    #
    @pytest.mark.p1
    @pytest.mark.db  
    def test_successfull_login_mm(self, base_url):
        logger.info("2222222222222222222running:::::::::::::test_successfull_login")
        LoginPage(self.driver) \
            .open_url(base_url) \
            .input_email('mm@macrometa.io') \
            .input_password("Macrometa123!@#") \
            .submit()

    #
    # Example: Using steps as an additional layer to implement domain driver design in automation framework
    #
    @pytest.mark.p3
    @pytest.mark.login
    def test_successfull_login_tenant(self, base_url):
        login_steps_obj = LoginSteps(self.driver)
        login_steps_obj.login_with_valid_credential(base_url, "sanjeet.singh@macrometa.com", "Macrometa123!@#")
        login_steps_obj.assert_dashboard_page_landing()
        pass
        