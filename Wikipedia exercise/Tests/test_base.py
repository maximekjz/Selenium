import pytest

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, init_driver):
        self.driver = init_driver
        yield
        self.driver.quit()
