from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class LoginPage(BasePage):

    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, "//button[contains(@class, 'submit-button') and .//span[text()='Sign In']]")
    SIGNIN_TITLE = (By.XPATH, "//h1[contains(@class, 'login-page__title') and text()='Sign In']")

    """CONSTRUCTOR OF THE PAGE CLASS"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """Page Actions"""

    """This is used to get the page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """This is used to check sign in link"""
    def is_signin_title_exist(self):
        return self.is_visible(self.SIGNIN_TITLE)

    """This is used to login to app"""
    def do_login(self, username, password):
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)


