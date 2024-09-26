import pytest
from selenium import webdriver
from Config.config import TestData
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(params=["chrome"], scope="class")
def init_driver(request):
    if request.param == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        yield driver
        driver.quit()