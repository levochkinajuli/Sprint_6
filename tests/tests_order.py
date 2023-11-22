from locators import MainPageLocators
from data import Urls, Data
from pages.main_page import MainPageSamokat
from pages.order_page import OrderPageSamokat
import time
from conftest import browser


class TestOrderPage:

    def test_success_order_up_button(self, browser):
        MainPageSamokat(browser).get_cookies(MainPageLocators.BUTT_COOKIES)
        OrderPageSamokat(browser).make_order_up_button(Data.name, Data.surname, Data.address, Data.phone, Data.comment)
        assert OrderPageSamokat(browser).check_success_order()

    def test_success_order_down_button(self, browser):
        MainPageSamokat(browser).get_cookies(MainPageLocators.BUTT_COOKIES)
        OrderPageSamokat(browser).make_order_down_button(Data.name2, Data.surname2, Data.address2, Data.phone2, Data.comment2)
        assert OrderPageSamokat(browser).check_success_order()

    def test_switch_to_dzen_page(self, browser):
        MainPageSamokat(browser).get_cookies(MainPageLocators.BUTT_COOKIES)
        OrderPageSamokat(browser).click_ya_logo()
        window_handles = browser.window_handles
        browser.switch_to.window(window_handles[1])
        time.sleep(7)
        element = MainPageSamokat(browser).get_text(MainPageLocators.DZENMAIN)
        assert 'В Дзене применяются' in element

    def test_click_on_logo_samokat(self, browser):
        OrderPageSamokat(browser).click_to_element(MainPageLocators.BUTT_ORDER_UP)
        OrderPageSamokat(browser).click_samokat_logo()
        expected_url = Urls.MAIN_PAGE
        assert browser.current_url == expected_url
