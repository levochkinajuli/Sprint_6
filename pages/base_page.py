from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 2).until(
            expected_conditions.visibility_of_element_located(locator))

    def click_to_element(self, locator):
        element = self.find_element(locator)
        if element:
            try:
                element.click()
            except Exception as e:
                print(f"Ошибка при клике на элемент: {e}")

    def get_text(self, locator):
        return WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator)).text

    def scroll(self, locator):
        last_element = self.find_element(locator)
        return self.driver.execute_script("arguments[0].scrollIntoView();", last_element)

    def get_cookies(self, locator):
        element = WebDriverWait(self.driver, 3).until(
            expected_conditions.visibility_of_element_located(locator))
        return element.click()

