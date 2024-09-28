from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver


    def do_click(self, by_locator):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element(self, by_locator):
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver,10).until(EC.title_is(title))
        return self.driver.title

    def is_url_new(self, url):
        try:
            WebDriverWait(self.driver, 10).until(EC.url_changes(url))
            return self.driver.current_url != url
        except TimeoutException:
            return False

    def visibility(self, by_locator):
        elements = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return bool(elements)


