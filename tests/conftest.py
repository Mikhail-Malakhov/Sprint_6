import pytest
from selenium import webdriver

from pages.main_page import MainPage
from pages.order_page import OrderPage


def pytest_addoption(parser):
    parser.addoption('--headless', action='store_true', help='Запускать Firefox без интерфейса')


@pytest.fixture
def driver(request):
    options = webdriver.FirefoxOptions()
    if request.config.getoption('--headless'):
        options.add_argument('-headless')
    driver = webdriver.Firefox(options=options)
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.open_main_page()
    return page


@pytest.fixture
def order_page(driver):
    return OrderPage(driver)
