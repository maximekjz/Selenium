from selenium.webdriver.common.by import By
from .search_result_page import SearchResult
from Config.config import TestData
from .BasePage import BasePage
from selenium.common.exceptions import TimeoutException

class HomePage(BasePage):

    #Log in variables
    USERNAME = (By.ID, 'wpName1')
    PASSWORD = (By.ID, 'wpPassword1')
    LOGIN_BUTTON = (By.ID, 'wpLoginAttempt')
    LOG_IN_LINK = (By.XPATH, "//a[span[text()='Log in']]")
    KEEP_LOGGED_IN = (By.ID, '.wpRemember')
    FEATURED_ARTICLE_TITLE = (By.ID, "From_today's_featured_article")
    FEATURED_ARTICLE_CONTENT = (By.ID, "From_today.27s_featured_article")
    DID_U_KNOW_TITLE = (By.ID, "Did_you_know_...")
    DID_U_KNOW_CONTENT = (By.ID, "mp-dyk")
    SISTER_PROJECTS = (By.ID, "Wikipedia's_sister_projects")
    WELCOME = (By.ID, 'mp-welcomecount')
    LANGUAGE_DROPDOWN = (By.ID, "p-lang-btn-checkbox")
    LANGUAGE_CHOSEN = (By.XPATH, '//a[@class="autonym" and @lang="he" and @dir="rtl"]')
    SEARCH_BUTTON = (By.CLASS_NAME, "cdx-search-input__end-button")
    SEARCH_FIELD = (By.CLASS_NAME, '.cdx-text-input__input')
    SEARCH_SUGGESTIONS = (By.CLASS_NAME, '.cdx-menu-item__text')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.MAIN_URL)

    """Used"""
    def go_to_login_page(self):
        self.driver.get(TestData.LOG_URL)

    def do_login(self, username, password):
        try:
            self.do_send_keys(self.USERNAME, username)
            self.do_send_keys(self.PASSWORD, password)
            #self.do_click(self.KEEP_LOGGED_IN).   Why it doesn't work ?
            self.do_click(self.LOGIN_BUTTON)
            return HomePage(self.driver)
        except TimeoutException as e:
            print(f"Error during login: {str(e)}")
            print(f"Current URL: {self.driver.current_url}")
            print(f"Page source: {self.driver.page_source}")
            raise

    def is_login_title_exists(self):
        return self.is_visible(self.LOG_IN_LINK)

    def new_url(self):
        self.is_url_new(TestData.LOG_URL)

    def check_visibility_of_elements(self):
        elements = [
            self.FEATURED_ARTICLE_TITLE,
            self.FEATURED_ARTICLE_CONTENT,
            self.DID_U_KNOW_TITLE,
            self.DID_U_KNOW_CONTENT,
            self.SISTER_PROJECTS
        ]
        return all(self.is_visible(element) for element in elements)

    def is_search_button_visible(self):
        return self.is_visible(self.SEARCH_BUTTON)

    def is_search_field_visible(self):
        return self.is_visible(self.SEARCH_FIELD)

    def is_search_suggestions_visible(self):
        return self.is_visible(self.SEARCH_SUGGESTIONS)

    def change_language(self):
        self.do_click(self.LANGUAGE_DROPDOWN)
        self.do_send_keys(self.LANGUAGE_CHOSEN)
        return HomePage(self.driver)
    '''Stop'''

    def do_search(self, search_content):
        self.do_send_keys(self.SEARCH_FIELD, search_content)
        self.do_click(self.SEARCH_BUTTON)
        return SearchResult(self.driver)

    def enter_search_term(self, partial_term):
        self.do_send_keys(self.SEARCH_FIELD, partial_term)

