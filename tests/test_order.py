import allure
import pytest

from data import ORDER_DATA


@allure.feature('Заказ самоката')
class TestOrder:

    @allure.title('Позитивный сценарий заказа через кнопку «Заказать» ({entry_point})')
    @pytest.mark.parametrize(
        'entry_point, order_data',
        [('top', ORDER_DATA[0]), ('bottom', ORDER_DATA[1])],
        ids=['top_button', 'bottom_button'],
    )
    def test_order_scooter_success(self, main_page, order_page, entry_point, order_data):
        main_page.click_order_button(entry_point)
        order_page.make_order(order_data)

        assert order_page.is_success_modal_displayed()
