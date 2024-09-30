from .test_base import BaseTest
from Pages.home_page import HomePage
from Config.config import TestData

class Test_Home(BaseTest):

    def log_in_route(self):
        self.homePage = HomePage(self.driver)
        assert HomePage.is_login_title_exists()

    def test_login(self):
        self.homePage = HomePage(self.driver)
        self.homePage.go_to_login_page()
        self.homePage.new_url()
        self.homePage.do_login(TestData.ACCOUNT_NAME, TestData.PASSWORD)

    def elements_visibility(self):
        self.homePage = HomePage(self.driver)
        assert HomePage.check_visibility_of_elements(), "Not all home page elements are visible"

    def search_button_visibility(self):
        self.homePage = HomePage(self.driver)
        assert HomePage.is_search_button_visible()

    def search_field_visibility(self):
        self.homePage = HomePage(self.driver)
        assert HomePage.is_search_button_visible()

    def search_sugg_visibility(self):
        self.homePage = HomePage(self.driver)
        assert HomePage.is_seach_suggestions_visible()

    def change_language_action(self):
        self.homePage = HomePage(self.driver)
        assert HomePage.change_language(TestData.LANGUAGE)

    def input_search(self):
        self.homePage = HomePage(self.driver)
        assert HomePage.do_search()

    def search(self):
        self.homePage = HomePage(self.driver)
        assert HomePage.enter_search_term()



