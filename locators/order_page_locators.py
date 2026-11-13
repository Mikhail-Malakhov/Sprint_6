from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Шаг 1 — «Для кого самокат»
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_NextButton')]/button[text()='Далее']")

    @staticmethod
    def metro_option(station):
        return By.XPATH, f"//div[contains(@class, 'Order_Text') and text()='{station}']"

    # Шаг 2 — «Про аренду»
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-control')
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    @staticmethod
    def rental_period_option(period):
        return By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']"

    @staticmethod
    def color_checkbox(color_id):
        return By.ID, color_id

    # Модальные окна
    CONFIRM_YES_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Да']")
    SUCCESS_MODAL_HEADER = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")
