from selenium.webdriver.common.by import By
from .BasePage import BasePage
class SearchResult(BasePage):

    SEARCH_BUTTON = (By.CSS_SELECTOR,'cdx-button cdx-button--action-default cdx-button--weight-normal cdx-button--size-medium cdx-button--framed cdx-search-input__end-button')
    SEARCH_FIELD = (By.CSS_SELECTOR,'cdx-text-input cdx-text-input--has-start-icon cdx-text-input--status-default cdx-search-input__text-input')
    SEARCH_RESULTS = (By.CSS_SELECTOR, ".mw-search-results")
    EMPTY_SEARCH_ERROR = (By.CSS_SELECTOR, ".mw-search-nonefound")

    def __init__(self, driver):
        super().__init__(driver)

    def do_search(self, search_content):
        self.do_send_keys(self.SEARCH_FIELD, search_content)
        self.do_click(self.SEARCH_BUTTON)
        return SearchResult(self.driver)

    def is_search_button_visible(self):
        return self.is_visible(self.SEARCH_BUTTON)

    def is_search_field_visible(self):
        return self.is_visible(self.SEARCH_FIELD)

    def is_at_search_result_page(self):
        return self.is_visible(self.SEARCH_RESULTS)

    def search_results_contain(self, search_term):
        results_text = self.get_element_text(self.SEARCH_RESULTS)
        return search_term.lower() in results_text.lower()

    def empty_search_error_displayed(self):
        return self.is_visible(self.EMPTY_SEARCH_ERROR)


