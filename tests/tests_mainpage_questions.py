from locators import MainPageLocators
from pages.main_page import MainPageSamokat
from data import TextOfTheAnswers
import pytest
import time
from conftest import browser


class TestQuestionsMainPage:

    @pytest.mark.parametrize('number, expected_answer',
                             [[0, TextOfTheAnswers.answer_0_text],
                              [1, TextOfTheAnswers.answer_1_text],
                              [2, TextOfTheAnswers.answer_2_text],
                              [3, TextOfTheAnswers.answer_3_text],
                              [4, TextOfTheAnswers.answer_4_text],
                              [5, TextOfTheAnswers.answer_5_text],
                              [6, TextOfTheAnswers.answer_6_text],
                              [7, TextOfTheAnswers.answer_7_text]
                              ])
    def test_question_get_correct_answer(self, browser, number, expected_answer):
        last_element = browser.find_element(*MainPageLocators.QUESTION_LOCATOR_7)
        browser.execute_script("arguments[0].scrollIntoView();", last_element)
        MainPageSamokat(browser).get_question(number)

        answer = MainPageSamokat(browser).get_answer(number)
        time.sleep(2)
        assert answer == expected_answer
