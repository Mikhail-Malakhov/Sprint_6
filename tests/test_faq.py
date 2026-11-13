import allure
import pytest

from data import FAQ


@allure.feature('Главная страница')
@allure.story('Раздел «Вопросы о важном»')
class TestFaq:

    @allure.title('При нажатии на вопрос «{question}» открывается соответствующий ответ')
    @pytest.mark.parametrize('index, question, answer', FAQ, ids=[f'question_{item[0]}' for item in FAQ])
    def test_faq_answer_opens_on_click(self, main_page, index, question, answer):
        main_page.click_faq_question(index)

        assert main_page.get_faq_question(index) == question
        assert main_page.get_faq_answer(index) == answer
