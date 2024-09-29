from .test_base import BaseTest
from Pages.home_page import HomePage
from Config.config import TestData

class Test_Home(BaseTest):


    def test_signin_link_visible(self):
        self.homePage = HomePage(self.driver)
        assert self.homePage.is_signin_link_exists(), "Sign-in link is not visible"

    def test_login_page_title(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_logged_in_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_login(TestData.USER_NAME, TestData.PASSWORD)

    def test_home_page_elements(self):
        self.homePage = HomePage(self.driver)
        self.homePage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        assert self.homePage.check_visibility_of_elements(), "Not all home page elements are visible"




