from .test_base import BaseTest
from Pages.home_page import HomePage
from Config.config import TestData

class Test_Home(BaseTest):

    # def test_log_in_route(self):
    #    self.homePage = HomePage(self.driver)
    #    assert self.homePage.is_login_title_exists()

    # def test_login(self):
    #     self.homePage = HomePage(self.driver)
    #     self.homePage.go_to_login_page()
    #     self.homePage.new_url()
    #     self.homePage.do_login(TestData.ACCOUNT_NAME, TestData.PASSWORD)

    # def test_elements_visibility(self):
    #     self.homePage = HomePage(self.driver)
    #     assert self.homePage.check_visibility_of_elements()
    #
    # def test_search_button_visibility(self):
    #     self.homePage = HomePage(self.driver)
    #     assert self.homePage.is_search_button_visible()
    #
    # def test_search_field_visibility(self):
    #     self.homePage = HomePage(self.driver)
    #     assert self.homePage.is_search_field_visible()
    #
    # def test_search_sugg_visibility(self):
    #     self.homePage = HomePage(self.driver)
    #     assert self.homePage.is_search_suggestions_visible()
    #
    # def test_change_language_action(self):
    #     self.homePage = HomePage(self.driver)
    #     assert self.homePage.change_language(TestData.LANGUAGE)
    #
    # def test_input_search(self):
    #     self.homePage = HomePage(self.driver)
    #     assert self.homePage.do_search()
    #
    # def test_search(self):
    #     self.homePage = HomePage(self.driver)
    #     assert self.homePage.enter_search_term()



