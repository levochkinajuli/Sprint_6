from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = [By.ID, "accordion__heading-{}"]
    ANSWER_LOCATOR = [By.ID, "accordion__panel-{}"]
    BUTT_COOKIES = By.ID, "rcc-confirm-button"
    BUTT_ORDER_UP = By.CLASS_NAME, "Button_Button__ra12g"
    BUTT_ORDER_DOWN = By.CLASS_NAME, "Button_Button__ra12g.Button_Middle__1CSJM"
    QUESTION_LOCATOR_7 = (By.ID, "accordion__heading-7")


class OrderPageLocators:
    FIELD_NAME = By.CSS_SELECTOR, "input.Input_Input__1iN_Z[placeholder='* Имя']"
    FIELD_SURNAME = By.CSS_SELECTOR, "input.Input_Input__1iN_Z[placeholder='* Фамилия']"
    FIELD_ADDRESS = By.CSS_SELECTOR, "input.Input_Input__1iN_Z[placeholder='* Адрес: куда привезти заказ']"
    FIELD_METRO = By.CSS_SELECTOR, "input[placeholder='* Станция метро']"
    FIELD_PHONE = By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']"
    BUT_FURTHER = By.XPATH, ".//button[text()='Далее']"
    FIELD_WHEN = By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']"
    DATE_WHEN1 = By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--020']"
    DATE_WHEN2 = By.XPATH, "//div[@class='react-datepicker__day react-datepicker__day--022']"
    FIELD_TERM = By.XPATH, "//div[@class='Dropdown-placeholder' and contains(text(), 'Срок аренды')]"
    TERM1 = By.XPATH, "//div[@class='Dropdown-option' and contains(text(), 'сутки')]"
    TERM2 = By.XPATH, "//div[@class='Dropdown-option' and contains(text(), 'двое суток')]"
    BLACK = By.ID, "black"
    GREY = By.ID, "grey"
    COMMENTS = By.CSS_SELECTOR, "input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder='Комментарий для курьера']"
    BUT_BACK = By.XPATH, ".//button[text()='Назад']"
    BUT_ORDER = By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']"
    WANT_TO_ORDER = By.CLASS_NAME, "Order_ModalHeader__3FDaJ"
    BUT_YES = By.XPATH, ".//button[text()='Да']"
    BUT_NO = By.XPATH, ".//button[text()='Нет']"
    ORDER_ISSUED = By.CLASS_NAME, "Order_ModalHeader__3FDaJ"
    LOGO = By.CSS_SELECTOR, "img[src='/assets/scooter.svg'][alt='Scooter']"
    YA = By.CSS_SELECTOR, "img[src='/assets/ya.svg'][alt='Yandex']"
    M1 = By.XPATH, ".//li[@class='select-search__row' and @data-index='5' and @data-value='6']"
    M2 = By.XPATH, ".//li[@class='select-search__row' and @data-index='6' and @data-value='7']"
