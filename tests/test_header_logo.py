import allure

from pages.main_page import MainPage
from urls import BASE_URL, DZEN_URL


@allure.feature('Шапка сайта')
class TestHeaderLogo:

    @allure.title('Клик по логотипу «Самоката» ведёт на главную страницу')
    def test_scooter_logo_opens_main_page(self, driver, order_page):
        order_page.open_order_page()
        order_page.click_scooter_logo()

        assert MainPage(driver).is_main_page_opened()

    @allure.title('Клик по логотипу Яндекса открывает Дзен в новом окне')
    def test_yandex_logo_opens_dzen(self, main_page):
        main_page.click_yandex_logo()
        main_page.switch_to_new_window()

        assert main_page.wait_url_contains(DZEN_URL)
