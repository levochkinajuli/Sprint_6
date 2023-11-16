import pytest
from selenium import webdriver
from data import Urls
from locators import MainPageLocators

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.get(Urls.MAIN_PAGE)
    driver.find_element(*MainPageLocators.BUTT_COOKIES).click()

    yield driver
    driver.quit()
