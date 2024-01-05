from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def browser():
    # options = Options()
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


