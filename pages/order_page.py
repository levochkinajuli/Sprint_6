from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import OrderPageLocators, MainPageLocators
from pages.base_page import BasePage
import allure


class OrderPageSamokat(BasePage):

    @allure.step('Нажимаем кнопку "Заказать" вверху страницы')
    def push_button_order_up(self):
        return self.click_to_element(MainPageLocators.BUTT_ORDER_UP)

    @allure.step('Нажимаем кнопку "Заказать" внизу страницы')
    def push_button_order_down(self):
        return self.click_to_element(MainPageLocators.BUTT_ORDER_DOWN)

    @allure.step('Заполняем поле "Имя"')
    def set_name(self, name):
        return self.find_element(OrderPageLocators.FIELD_NAME).send_keys(name)

    @allure.step('Заполняем поле "Фамилия"')
    def set_surname(self, surname):
        return self.find_element(OrderPageLocators.FIELD_SURNAME).send_keys(surname)

    @allure.step('Заполняем поле "Адрес"')
    def set_address(self, address):
        return self.find_element(OrderPageLocators.FIELD_ADDRESS).send_keys(address)

    @allure.step('Выбираем станцию метро')
    def set_metro_1(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.FIELD_METRO))
        self.find_element(OrderPageLocators.FIELD_METRO).click()
        elem = WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.M1))
        return elem.click()

    @allure.step('Выбираем станцию метро')
    def set_metro_2(self):
        WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.FIELD_METRO))
        self.find_element(OrderPageLocators.FIELD_METRO).click()
        elem = WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.M2))
        return elem.click()

    @allure.step('Заполняем поле "Телефон"')
    def set_phone(self, phone):
        return self.find_element(OrderPageLocators.FIELD_PHONE).send_keys(phone)

    @allure.step('Нажимаем кнопку "Далее"')
    def click_further(self):
        return self.click_to_element(OrderPageLocators.BUT_FURTHER)

    @allure.step('Выбираем дату')
    def set_date_1(self):
        self.click_to_element(OrderPageLocators.FIELD_WHEN)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.DATE_WHEN1))
        return self.click_to_element(OrderPageLocators.DATE_WHEN1)

    @allure.step('Выбираем дату')
    def set_date_2(self):
        self.click_to_element(OrderPageLocators.FIELD_WHEN)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.DATE_WHEN2))
        return self.click_to_element(OrderPageLocators.DATE_WHEN2)

    @allure.step('Выбираем срок аренды')
    def set_term_1(self):
        self.click_to_element(OrderPageLocators.FIELD_TERM)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.TERM1))
        return self.click_to_element(OrderPageLocators.TERM1)

    @allure.step('Выбираем срок аренды')
    def set_term_2(self):
        self.click_to_element(OrderPageLocators.FIELD_TERM)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.TERM2))
        return self.click_to_element(OrderPageLocators.TERM2)

    @allure.step('Выбираем цвет')
    def set_color_grey(self):
        return self.click_to_element(OrderPageLocators.GREY)

    @allure.step('Выбираем цвет')
    def set_color_black(self):
        return self.click_to_element(OrderPageLocators.BLACK)

    @allure.step('Заполянем поле "Комментарии"')
    def set_comments(self, comments):
        return self.find_element(OrderPageLocators.COMMENTS).send_keys(comments)

    @allure.step('Ждем появления сообщения "Заказ создан"')
    def check_success_order(self):
        return WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_ISSUED))

    def make_order_up_button(self, name, surname, address, phone, comments):
        self.push_button_order_up()
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro_1()
        self.set_phone(phone)
        self.click_further()
        WebDriverWait(self.driver, 5).until(
             expected_conditions.visibility_of_element_located(OrderPageLocators.BUT_BACK))
        self.set_date_1()
        self.set_term_1()
        self.set_color_grey()
        self.set_comments(comments)
        self.click_to_element(OrderPageLocators.BUT_ORDER)
        self.click_to_element(OrderPageLocators.BUT_YES)

    def make_order_down_button(self, name, surname, address, phone, comments):
        self.push_button_order_down()
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro_2()
        self.set_phone(phone)
        self.click_further()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.BUT_BACK))
        self.set_date_2()
        self.set_term_2()
        self.set_color_black()
        self.set_comments(comments)
        self.click_to_element(OrderPageLocators.BUT_ORDER)
        self.click_to_element(OrderPageLocators.BUT_YES)

    @allure.step('Нажимаем на логотип Яндекс')
    def click_ya_logo(self):
        return self.click_to_element(OrderPageLocators.YA)

    @allure.step('Нажимаем на логотип Самокат')
    def click_samokat_logo(self):
        return self.find_element(OrderPageLocators.LOGO).click()
