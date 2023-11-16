from locators import MainPageLocators
from data import Urls, Data
from pages.order_page import OrderPageSamokat
import time
from conftest import browser


class TestOrderPage:

    def test_success_order_up_button(self, browser):
        OrderPageSamokat(browser).make_order_up_button(Data.name, Data.surname, Data.address, Data.phone, Data.comment)
        assert OrderPageSamokat(browser).check_success_order()

    def test_success_order_down_button(self, browser):
        OrderPageSamokat(browser).make_order_down_button(Data.name2, Data.surname2, Data.address2, Data.phone2, Data.comment2)
        assert OrderPageSamokat(browser).check_success_order()

    def test_switch_to_dzen_page(self, browser):
        OrderPageSamokat(browser).click_ya_logo()
        time.sleep(5)
        window_handles = browser.window_handles
        browser.switch_to.window(window_handles[1])
        current_url = browser.current_url
        expected_url = Urls.DZEN_PAGE
        assert current_url == expected_url

    def test_click_on_logo_samokat(self, browser):
        OrderPageSamokat(browser).click_to_element(MainPageLocators.BUTT_ORDER_UP)
        OrderPageSamokat(browser).click_samokat_logo()
        expected_url = Urls.MAIN_PAGE
        assert browser.current_url == expected_url
