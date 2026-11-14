from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Шаг 1 — «Для кого самокат»
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//button[contains(@class, 'Order_SelectOption')]/div[text()='{}']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Шаг 2 — «Про аренду»
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-control')
    RENTAL_PERIOD_OPTION = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")
    COLOR_CHECKBOX = (By.ID, '{}')
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Назад']/following-sibling::button[text()='Заказать']")

    # Модальные окна
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL_HEADER = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
