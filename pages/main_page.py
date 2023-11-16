from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from locators import MainPageLocators
from pages.base_page import BasePage


class MainPageSamokat(BasePage):
    @allure.step('Принимаем куки')
    def get_cookies(self):
        return WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.BUTT_COOKIES)).click()

    @allure.step('Нажимаем на вопрос')
    def get_question(self, number):
        method, locator = MainPageLocators.QUESTION_LOCATOR
        locator = locator.format(number)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((method, locator)))
        return self.click_to_element((method, locator))

    @allure.step('Получаем ответ на вопрос')
    def get_answer(self, number):
        method, locator = MainPageLocators.ANSWER_LOCATOR
        locator = locator.format(number)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located((method, locator)))
        return self.get_text((method, locator))
