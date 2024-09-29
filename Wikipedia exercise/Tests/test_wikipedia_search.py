import pytest
from .test_base import BaseTest
from Config.config import TestData
from Pages.home_page import HomePage


class TestWikipediaSearch(BaseTest):
    @pytest.fixture(autouse=True)
    def setup(self, init_driver):
        self.driver = init_driver
        self.home_page = HomePage(self.driver)

    def test_search_functionality(self):
        search_page = self.home_page.do_search(TestData.SEARCH_FIELD_CONTENT)
        assert search_page.is_at_search_result_page(), "Not on search result page"
        assert search_page.search_results_contain(TestData.SEARCH_FIELD_CONTENT), "Search results do not contain the search term"

    def test_search_button_visible(self):
        assert self.home_page.is_search_button_visible(), "Search button is not visible"

    def test_search_field_visible(self):
        assert self.home_page.is_search_field_visible(), "Search field is not visible"

    def test_empty_search(self):
        search_page = self.home_page.do_search("")
        assert search_page.empty_search_error_displayed(), "Empty search error message not displayed"

    def test_search_suggestion(self):
        self.home_page.enter_search_term(TestData.SEARCH_FIELD_CONTENT[:3])
        assert self.home_page.search_suggestions_visible(), "Search suggestions are not visible"

    def test_search_and_verify_first_result(self):
        search_page = self.home_page.do_search(TestData.SEARCH_FIELD_CONTENT)
        first_result_title = search_page.get_first_result_title()
        assert TestData.SEARCH_FIELD_CONTENT.lower() in first_result_title.lower(), f"First result '{first_result_title}' does not contain search term '{TestData.SEARCH_FIELD_CONTENT}'"

