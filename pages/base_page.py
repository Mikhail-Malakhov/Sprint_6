import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators.header_locators import HeaderLocators


class BasePage:
    TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def format_locator(locator, *args):
        by, value = locator
        return by, value.format(*args)

    @allure.step('Открыть страницу {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Дождаться видимости элемента {locator}')
    def wait_visible(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(locator))

    @allure.step('Дождаться кликабельности элемента {locator}')
    def wait_clickable(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.element_to_be_clickable(locator))

    @allure.step('Найти элемент {locator}')
    def find(self, locator):
        return self.wait_visible(locator)

    @allure.step('Кликнуть по элементу {locator}')
    def click(self, locator):
        self.wait_clickable(locator).click()

    @allure.step('Прокрутить страницу до элемента {locator}')
    def scroll_to(self, locator):
        element = WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_element_located(locator))
        self.driver.execute_script('arguments[0].scrollIntoView({block: "center"});', element)
        return element

    @allure.step('Ввести текст «{text}» в поле {locator}')
    def type_text(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    @allure.step('Получить текст элемента {locator}')
    def get_text(self, locator):
        return self.find(locator).text

    @allure.step('Проверить, что элемент {locator} отображается')
    def is_displayed(self, locator):
        return self.find(locator).is_displayed()

    @allure.step('Получить текущий URL')
    def current_url(self):
        return self.driver.current_url

    @allure.step('Дождаться, что URL содержит {part}')
    def wait_url_contains(self, part):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.url_contains(part))
        return self.driver.current_url

    @allure.step('Дождаться, что URL равен {url}')
    def wait_url_to_be(self, url):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.url_to_be(url))
        return self.driver.current_url

    @allure.step('Нажать на логотип «Самоката»')
    def click_scooter_logo(self):
        self.click(HeaderLocators.SCOOTER_LOGO)

    @allure.step('Нажать на логотип Яндекса')
    def click_yandex_logo(self):
        self.click(HeaderLocators.YANDEX_LOGO)

    @allure.step('Переключиться на новую вкладку')
    def switch_to_new_window(self):
        original = self.driver.current_window_handle
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.number_of_windows_to_be(2))
        new_window = next(handle for handle in self.driver.window_handles if handle != original)
        self.driver.switch_to.window(new_window)
