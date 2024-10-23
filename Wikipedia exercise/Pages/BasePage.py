from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)



    def do_click(self, by_locator):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def do_send_keys_actions_chains(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

        self.actions.click(element)
        self.actions.send_keys(text)
        self.actions.perform()

    def get_element(self, by_locator):
        element = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
            return bool(element)
        except TimeoutException:
            return False

    def is_url_new(self, url):
        try:
            WebDriverWait(self.driver, 10).until(EC.url_changes(url))
            return self.driver.current_url != url
        except TimeoutException:
            return False

    def visibility(self, by_locator):
        elements = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return bool(elements)

    def press_enter(self):
        self.actions.send_keys(Keys.ENTER).perform()

    def get_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def assert_equal(self, expected_value, fetched_value):
        assert expected_value == fetched_value, f"Expected {expected_value} to be equal to {fetched_value}, but they are not!"



