from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    ORDER_BUTTON_TOP = (By.XPATH, "//button[text()='Статус заказа']/preceding-sibling::button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    HOME_HEADER = (By.XPATH, "//div[contains(@class, 'Home_Header')]")

    # Шаблоны: номер вопроса подставляется в BasePage.format_locator
    FAQ_QUESTION = (By.ID, 'accordion__heading-{}')
    FAQ_ANSWER = (By.XPATH, "//div[@id='accordion__panel-{}']/p")
