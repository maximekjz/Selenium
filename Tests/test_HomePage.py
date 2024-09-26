from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
from Config.config import TestData

class Test_Home(BaseTest):
    def test_home_page_title(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        title = homePage.get_home_page_title(TestData.HOME_PAGE_TITLE)
        assert title == TestData.HOME_PAGE_TITLE

    def test_home_page_header(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        header = homePage.get_header_value()
        assert header == TestData.HOME_PAGE_HEADER

    def test_home_page_watch_button(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        assert homePage.is_watch_button_exists()


    def test_home_page_menu(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        assert homePage.is_menu_exists()

    def test_home_page_search(self):
        self.loginPage = LoginPage(self.driver)
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        assert homePage.is_search_exists()


