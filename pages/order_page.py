import allure
from selenium.webdriver.common.keys import Keys

from locators.order_page_locators import OrderPageLocators
from helpers import future_date
from pages.base_page import BasePage
from urls import ORDER_URL


class OrderPage(BasePage):

    @allure.step('Открыть страницу заказа')
    def open_order_page(self):
        self.open(ORDER_URL)

    @allure.step('Заполнить форму «Для кого самокат»')
    def fill_customer_form(self, name, surname, address, metro, phone):
        self.type_text(OrderPageLocators.NAME_INPUT, name)
        self.type_text(OrderPageLocators.SURNAME_INPUT, surname)
        self.type_text(OrderPageLocators.ADDRESS_INPUT, address)
        self.select_metro(metro)
        self.type_text(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step('Выбрать станцию метро «{metro}»')
    def select_metro(self, metro):
        self.type_text(OrderPageLocators.METRO_INPUT, metro)
        self.click(self.format_locator(OrderPageLocators.METRO_OPTION, metro))

    @allure.step('Нажать кнопку «Далее»')
    def click_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить форму «Про аренду»')
    def fill_rent_form(self, date, rental_period, color, comment):
        self.set_date(date)
        self.select_rental_period(rental_period)
        self.click(self.format_locator(OrderPageLocators.COLOR_CHECKBOX, color))
        self.type_text(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step('Указать дату доставки {date}')
    def set_date(self, date):
        element = self.find(OrderPageLocators.DATE_INPUT)
        element.send_keys(date)
        element.send_keys(Keys.ENTER)

    @allure.step('Выбрать срок аренды «{period}»')
    def select_rental_period(self, period):
        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click(self.format_locator(OrderPageLocators.RENTAL_PERIOD_OPTION, period))

    @allure.step('Нажать кнопку «Заказать» в форме')
    def click_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтвердить заказ')
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step('Оформить заказ целиком')
    def make_order(self, data):
        self.fill_customer_form(data['name'], data['surname'], data['address'], data['metro'], data['phone'])
        self.click_next()
        self.fill_rent_form(future_date(data['delivery_in_days']), data['rental_period'], data['color'], data['comment'])
        self.click_order()
        self.confirm_order()

    @allure.step('Проверить, что появилось окно об успешном оформлении заказа')
    def is_success_modal_displayed(self):
        return self.is_displayed(OrderPageLocators.SUCCESS_MODAL_HEADER)
