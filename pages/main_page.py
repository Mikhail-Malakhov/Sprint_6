import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from urls import BASE_URL


class MainPage(BasePage):
    ORDER_BUTTONS = {
        'top': MainPageLocators.ORDER_BUTTON_TOP,
        'bottom': MainPageLocators.ORDER_BUTTON_BOTTOM,
    }

    @allure.step('Открыть главную страницу')
    def open_main_page(self):
        self.open(BASE_URL)
        self.accept_cookies()

    @allure.step('Принять куки')
    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Нажать на вопрос №{index} в разделе «Вопросы о важном»')
    def click_faq_question(self, index):
        locator = MainPageLocators.faq_question(index)
        self.scroll_to(locator)
        self.click(locator)

    @allure.step('Получить текст ответа на вопрос №{index}')
    def get_faq_answer(self, index):
        return self.get_text(MainPageLocators.faq_answer(index))

    @allure.step('Получить текст вопроса №{index}')
    def get_faq_question(self, index):
        return self.get_text(MainPageLocators.faq_question(index))

    @allure.step('Нажать кнопку «Заказать» ({position})')
    def click_order_button(self, position):
        locator = self.ORDER_BUTTONS[position]
        self.scroll_to(locator)
        self.click(locator)

    @allure.step('Проверить, что открыта главная страница')
    def is_main_page_opened(self):
        return self.current_url() == BASE_URL and self.is_displayed(MainPageLocators.HOME_HEADER)
