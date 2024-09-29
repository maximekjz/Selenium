from .test_base import BaseTest
from Pages.home_page import HomePage
from Config.config import TestData

class Test_Home(BaseTest):

    def test_login(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_to_login_page()
        self.homePage.do_login(TestData.ACCOUNT_NAME, TestData.PASSWORD)
        assert self.homePage.check_visibility_of_elements(), "Not all home page elements are visible"




