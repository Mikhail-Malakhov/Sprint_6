from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_BUTTON = (By.ID, 'rcc-confirm-button')
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[text()='Заказать']")
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[text()='Заказать']")
    FAQ_SECTION = (By.CLASS_NAME, 'Home_FAQ__3uVm4')
    HOME_HEADER = (By.XPATH, "//div[contains(@class, 'Home_Header')]")

    @staticmethod
    def faq_question(index):
        return By.ID, f'accordion__heading-{index}'

    @staticmethod
    def faq_answer(index):
        return By.XPATH, f"//div[@id='accordion__panel-{index}']/p"
