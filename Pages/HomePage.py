from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class HomePage(BasePage):

    """Check with class"""
    HEADER = (By.CSS_SELECTOR, 'a.flex items-center self-center')
    MENU = (By.CSS_SELECTOR, 'BurgerMenuButton')
    SEARCH = (By.CSS_SELECTOR, 'a.flex relative items-center bg-transparent px-3 transition-colors hover:bg-fill-03 active:bg-fill-02')

    """Other way to check"""
    WATCH_BUTTON = (By.CSS_SELECTOR, "a[href='/watch/'][data-testid='link-organism-mobile-sub-navigation-item']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_home_page(self, title):
        return self.get_title(title)

    def is_watch_button_exists(self):
        return self.is_visible(self.WATCH_BUTTON)

    def is_menu_exists(self):
        return self.is_visible(self.MENU)

    def is_search_exists(self):
        return self.is_visible(self.SEARCH)

    def get_header_value(self):
        return self.get_element_text(self.HEADER)



