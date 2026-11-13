# Sprint_6 — UI-автотесты «Яндекс.Самокат»

Стек: Python, pytest, Selenium (Firefox), Allure. Паттерн Page Object.

## Структура
- `locators/` — локаторы для каждой страницы
- `pages/` — Page Object: `BasePage`, `MainPage`, `OrderPage`
- `tests/` — тесты:
  - `test_faq.py` — выпадающий список «Вопросы о важном» (8 вопросов, параметризация)
  - `test_order.py` — позитивный заказ: верхняя и нижняя кнопки «Заказать», два набора данных (параметризация)
  - `test_header_logo.py` — логотип «Самоката» ведёт на главную, логотип Яндекса открывает Дзен в новом окне
- `data.py` — тестовые данные, `urls.py` — адреса

## Запуск
```bash
pip install -r requirements.txt
pytest                 # результаты Allure пишутся в allure-results
pytest --headless      # без окна браузера
allure serve allure-results
```
