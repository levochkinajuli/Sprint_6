import pytest
from selenium import webdriver
from data import Urls

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.get(Urls.MAIN_PAGE)

    yield driver
    driver.quit()
